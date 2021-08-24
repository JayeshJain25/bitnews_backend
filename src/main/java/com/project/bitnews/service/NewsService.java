package com.project.bitnews.service;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.mongo.model.NewsModel;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
public class NewsService {

    public static final String DB_NAME_CRYPT_LIST = "CryptoFiatList";

    @Autowired
    MongoTemplate mongoTemplate;

    public List<CryptoAndFiatModel> getAllCryptoAndFiatList() {
        return mongoTemplate.findAll(CryptoAndFiatModel.class);
    }

    public List<NewsModel> getAllNewsList() {
        return mongoTemplate.findAll(NewsModel.class);
    }
}
