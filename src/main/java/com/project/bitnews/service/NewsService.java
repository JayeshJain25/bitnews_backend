package com.project.bitnews.service;

import com.project.bitnews.mongo.model.NewsModel;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
public class NewsService {

    @Autowired
    MongoTemplate mongoTemplate;

    public List<NewsModel> getAllNewsList() {
        Query query = new Query();
        query.with(Sort.by(Sort.Direction.DESC, "publishedDate"));
        return mongoTemplate.find(query,NewsModel.class);
    }
}
