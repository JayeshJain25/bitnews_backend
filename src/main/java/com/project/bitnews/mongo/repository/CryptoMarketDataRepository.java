package com.project.bitnews.mongo.repository;

import org.springframework.data.mongodb.repository.Query;
import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CryptoMarketDataRepository extends MongoRepository<CryptoCurrencyMarketDataModel,String> {
    @Query("{rank : {$gte : ?0} }")
    Page<CryptoCurrencyMarketDataModel> findAll(double rank,Pageable pageable);
    }