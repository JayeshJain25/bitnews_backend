package com.project.bitnews.scheduler;

import com.mongodb.bulk.BulkWriteResult;
import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import com.project.bitnews.utils.csv.CryptoCurrencyListCsv;
import com.project.bitnews.utils.csv.CryptoCurrencyMarketDataListCsv;
import org.springframework.data.mongodb.core.BulkOperations;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

@Component
public class CryptoCurrencyMarketDataList {

    String basePath = new File("").getAbsolutePath();
    String cryptoCurrencyMarketData = basePath + "/python/cryptocurrencyData.py";
    String cryptoCurrencyMarketDataPath = basePath + "/cryptoCoinsMarketData.csv";
    String cryptoPriceListPath = basePath + "/cryptoCurrencyPrices.csv";

    final MongoTemplate mongoTemplate;

    public CryptoCurrencyMarketDataList(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Scheduled(fixedRate = 120000)
    private void cryptoCoinsMarketData() throws IOException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: CryptoCoinsMarketData -> " + strDate);

        Runtime.getRuntime().exec("python3 " + cryptoCurrencyMarketData);

        List<CryptoAndFiatModel> cryptoAndFiatModelList = CryptoCurrencyListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(cryptoPriceListPath)));

        updateLivePriceData(cryptoAndFiatModelList);

        List<CryptoCurrencyMarketDataModel> cryptoCurrencyMarketDataModelList = CryptoCurrencyMarketDataListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(cryptoCurrencyMarketDataPath)));
        updateCryptoMarketData(cryptoCurrencyMarketDataModelList);

    }


    private void updateCryptoMarketData(List<CryptoCurrencyMarketDataModel> cryptoCurrencyMarketDataModelList) {


        BulkOperations bulkOps = mongoTemplate.bulkOps(BulkOperations.BulkMode.UNORDERED, CryptoCurrencyMarketDataModel.class);
        for(CryptoCurrencyMarketDataModel marketDataModel : cryptoCurrencyMarketDataModelList){
            Query query = new Query().addCriteria(new Criteria("_id").is(marketDataModel.getId()));
            Update update = new Update();

            update.set("price", marketDataModel.getPrice());
            update.set("marketCap", marketDataModel.getMarketCap());
            update.set("totalVolume", marketDataModel.getTotalVolume());
            update.set("rank", marketDataModel.getRank());
            update.set("high24h",marketDataModel.getHigh24h());
            update.set("low24h",marketDataModel.getLow24h());
            update.set("priceChange24h",marketDataModel.getPriceChange24h());
            update.set("priceChangePercentage24h",marketDataModel.getPriceChangePercentage24h());
            update.set("marketCapChange24h",marketDataModel.getMarketCapChange24h());
            update.set("marketCapChangePercentage24h",marketDataModel.getMarketCapChangePercentage24h());
            update.set("circulatingSupply",marketDataModel.getCirculatingSupply());
            update.set("totalSupply",marketDataModel.getTotalSupply());
            update.set("maxSupply",marketDataModel.getMaxSupply());
            update.set("atl",marketDataModel.getAtl());
            update.set("atlChangePercentage",marketDataModel.getAtlChangePercentage());
            update.set("atlDate",marketDataModel.getAtlDate());
            update.set("lastUpdated",marketDataModel.getLastUpdated());
            bulkOps.upsert(query,update);
        }
        BulkWriteResult results = bulkOps.execute();

    }


    private void updateLivePriceData(List<CryptoAndFiatModel> cryptoAndFiatModelList) {

        BulkOperations bulkOps = mongoTemplate.bulkOps(BulkOperations.BulkMode.UNORDERED, CryptoAndFiatModel.class);
        for (CryptoAndFiatModel person : cryptoAndFiatModelList) {
            Query query = new Query().addCriteria(new Criteria("_id").is(person.getId()));
            Update update = new Update();
            update.set("price", person.getPrice());
            update.set("marketCap", person.getMarketCap());
            update.set("totalVolume", person.getTotalVolume());
            update.set("rank", person.getRank());
            bulkOps.upsert(query,update);
        }
        BulkWriteResult results = bulkOps.execute();
    }

}
