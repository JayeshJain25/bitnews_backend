package com.project.bitnews.scheduler;

import com.project.bitnews.mongo.model.NewsModel;
import com.project.bitnews.utils.csv.NewsListCsv;
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
import java.util.Date;
import java.util.List;

@Component
public class newsDataList {
    String basePath = new File("").getAbsolutePath();
    String news1PythonPath = basePath + "/python/newsScrap1.py";
    String news1ListPath = basePath + "/news1.csv";
    String news2PythonPath = basePath + "/python/newsScrap2.py";
    String news2ListPath = basePath + "/news2.csv";
    String news3PythonPath = basePath + "/python/newsScrap3.py";
    String news3ListPath = basePath + "/news3.csv";

    final MongoTemplate mongoTemplate;

    public newsDataList(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Scheduled(fixedRate = 3600000)
    private void newsList1Update() throws IOException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date now = new Date();
        String strDate = sdf.format(now);
        System.out.println("Java cron job expression:: NewsList1 -> " + strDate);

        Runtime.getRuntime().exec("python3 " + news1PythonPath);
        Runtime.getRuntime().exec("python3 " + news2PythonPath);
        Runtime.getRuntime().exec("python3 " + news3PythonPath);

        List<NewsModel> newsModelList =
                NewsListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(news1ListPath)));
        List<NewsModel> newsModelList2 =
                NewsListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(news2ListPath)));
        List<NewsModel> newsModelList3 =
                NewsListCsv.parseCsvFile(new BufferedInputStream(new FileInputStream(news3ListPath)));

        updateNewsList1(newsModelList);
        updateNewsList1(newsModelList2);
        updateNewsList1(newsModelList3);
    }

    private void updateNewsList1(List<NewsModel> newsModelList) {

        for (NewsModel model : newsModelList) {
            Query query = new Query(Criteria.where("title").is(model.getTitle()));
            NewsModel newsModel = mongoTemplate.findOne(query,NewsModel.class);
            if(newsModel == null){
                mongoTemplate.insert(model);
            }
        }
    }
}
