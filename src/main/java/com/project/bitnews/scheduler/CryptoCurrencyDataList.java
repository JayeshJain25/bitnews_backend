package com.project.bitnews.scheduler;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.utils.ApacheCommonsCsvUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Component
public class CryptoCurrencyDataList {

    @Autowired
    MongoTemplate mongoTemplate;

    @Scheduled(fixedRate = 60000)
    public void getHeadValue() throws IOException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: " + strDate);
        Process p = Runtime.getRuntime().exec("python3 /home/jigse/IdeaProjects/bitnews/python/cryptoCoinList.py");

        String initialString = "/home/jigse/IdeaProjects/bitnews/Prices1.csv";
        List<CryptoAndFiatModel> cryptoAndFiatModelList = ApacheCommonsCsvUtil.parseCsvFile(new BufferedInputStream(new FileInputStream(initialString)));


        ArrayList<String> ids = new ArrayList<>();
        for (CryptoAndFiatModel cryptoAndFiatModel : cryptoAndFiatModelList) {
            ids.add(cryptoAndFiatModel.getId());
        }

        Query q = new Query(Criteria.where("_id").in(ids));

        mongoTemplate.findAllAndRemove(q, CryptoAndFiatModel.class);
        mongoTemplate.insertAll(cryptoAndFiatModelList);

    }

}
