package com.project.bitnews.mongo.repository;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CryptoMarketDataRepository extends MongoRepository<CryptoCurrencyMarketDataModel,String> {
        Page<CryptoCurrencyMarketDataModel> findAll(Pageable pageable);
        Page<CryptoCurrencyMarketDataModel> findByRank(double rank,Pageable pageable);
    }