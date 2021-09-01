package com.project.bitnews.scheduler;

import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import com.project.bitnews.utils.csv.CryptoCurrencyMarketDataListCsv;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Component
public class CryptoCurrencyMarketDataList {

    String basePath = new File("").getAbsolutePath();
    String cryptoCurrencyMarketData = basePath + "/python/cryptocurrencyData.py";
    String cryptoCurrencyMarketDataPath = basePath + "/cryptoCoinsMarketData.csv";

    final MongoTemplate mongoTemplate;

    public CryptoCurrencyMarketDataList(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Scheduled(fixedRate = 60000)
    private void cryptoCoinsMarketData() throws IOException{
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: CryptoCoinsMarketData -> " + strDate);

        Runtime.getRuntime().exec("python3 " + cryptoCurrencyMarketData);

        List<CryptoCurrencyMarketDataModel> cryptoCurrencyMarketDataModelList = CryptoCurrencyMarketDataListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(cryptoCurrencyMarketDataPath)));

        updateCryptoMarketData(cryptoCurrencyMarketDataModelList);
    }


    private void updateCryptoMarketData(List<CryptoCurrencyMarketDataModel> cryptoCurrencyMarketDataModelList) {
        ArrayList<String> ids = new ArrayList<>();
        for (CryptoCurrencyMarketDataModel cryptoCurrencyMarketDataModel : cryptoCurrencyMarketDataModelList) {
            ids.add(cryptoCurrencyMarketDataModel.getId());
        }

        Query q = new Query(Criteria.where("_id").in(ids));

        mongoTemplate.findAllAndRemove(q, CryptoCurrencyMarketDataModel.class);
        mongoTemplate.insertAll(cryptoCurrencyMarketDataModelList);
    }
}
