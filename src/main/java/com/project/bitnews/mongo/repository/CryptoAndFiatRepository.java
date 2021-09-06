package com.project.bitnews.mongo.repository;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CryptoAndFiatRepository extends MongoRepository<CryptoAndFiatModel,String> {
    Page<CryptoAndFiatModel> findAll(Pageable pageable);
    Page<CryptoAndFiatModel> findByRank(double rank,Pageable pageable);
}