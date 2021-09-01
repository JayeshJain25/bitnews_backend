package com.project.bitnews.scheduler;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.utils.csv.CryptoCurrencyListCsv;
import com.project.bitnews.utils.csv.FiatCurrencyListCsv;
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
public class CryptoCurrencyDataList {

    String basePath = new File("").getAbsolutePath();
    String cryptoPricePythonPath = basePath + "/python/cryptoCoinList.py";
    String cryptoPriceListPath = basePath + "/cryptoCurrencyPrices.csv";
    String fiatPricePythonPath = basePath + "/python/fiatList.py";
    String fiatPriceListPath = basePath + "/fiatPrices.csv";

    final MongoTemplate mongoTemplate;

    public CryptoCurrencyDataList(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Scheduled(fixedRate = 60000)
    private void cryptoCurrencyPricesUpdate() throws IOException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: CryptoCurrencyPrice -> " + strDate);

        Runtime.getRuntime().exec("python3 " + cryptoPricePythonPath);

        List<CryptoAndFiatModel> cryptoAndFiatModelList = CryptoCurrencyListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(cryptoPriceListPath)));

        updateLivePriceData(cryptoAndFiatModelList);

    }

    private void updateLivePriceData(List<CryptoAndFiatModel> cryptoAndFiatModelList) {
        ArrayList<String> ids = new ArrayList<>();
        for (CryptoAndFiatModel cryptoAndFiatModel : cryptoAndFiatModelList) {
            ids.add(cryptoAndFiatModel.getId());
        }

        Query q = new Query(Criteria.where("_id").in(ids));

        mongoTemplate.findAllAndRemove(q, CryptoAndFiatModel.class);
        mongoTemplate.insertAll(cryptoAndFiatModelList);
    }

    @Scheduled(fixedRate = 60000)
    private void fiatCurrencyPriceUpdate() throws IOException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: FiatCurrencyPrice -> " + strDate);

        Runtime.getRuntime().exec("python3 " + fiatPricePythonPath);

        List<CryptoAndFiatModel> cryptoAndFiatModelList = FiatCurrencyListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(fiatPriceListPath)));

        updateLivePriceData(cryptoAndFiatModelList);

    }
}