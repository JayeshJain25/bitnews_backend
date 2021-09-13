package com.project.bitnews.mongo.repository;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;

public interface CryptoAndFiatRepository extends MongoRepository<CryptoAndFiatModel,String> {
    @Query("{rank : {$gte : ?0} }")
    Page<CryptoAndFiatModel> findAll(double rank,Pageable pageable);
    @Query("{ 'name' : { $regex: ?0, $options : 'i' } }")
    List<CryptoAndFiatModel> findByNameStartingWith(String name);
}
