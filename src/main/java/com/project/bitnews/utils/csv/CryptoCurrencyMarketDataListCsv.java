package com.project.bitnews.utils.csv;

import com.project.bitnews.mongo.model.CryptoCurrencyMarketDataModel;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class CryptoCurrencyMarketDataListCsv {


    public static List<CryptoCurrencyMarketDataModel> parseCsvFile(InputStream is) {
        BufferedReader fileReader = null;
        CSVParser csvParser = null;

        List<CryptoCurrencyMarketDataModel> cryptoAndFiatModelArrayList = new ArrayList<>();

        try {
            fileReader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            csvParser = new CSVParser(fileReader,
                    CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());

            Iterable<CSVRecord> csvRecords = csvParser.getRecords();

            for (CSVRecord csvRecord : csvRecords) {
                double totalSupply;
                double maxSupply;
                double high24h;
                double low24h;
                double marketCapChangePer24h;
                double priceChange24h;
                double priceChangePer24h;
                double marketCapChange24h;
                double price;
                double rank;
                double totalVolume;
                double marketCap;
                double circulatingSupply;
                double alt;
                double atlChangePercentage;

                if(!csvRecord.get("total_supply").isEmpty()){
                    totalSupply = Double.parseDouble(csvRecord.get("total_supply"));
                }else{
                    totalSupply = 0;
                }
                if(!csvRecord.get("max_supply").isEmpty()){
                    maxSupply = Double.parseDouble(csvRecord.get("max_supply"));
                }else{
                    maxSupply = 0;
                }if(!csvRecord.get("high_24h").isEmpty()){
                    high24h = Double.parseDouble(csvRecord.get("high_24h"));
                }else{
                    high24h = 0;
                }if(!csvRecord.get("low_24h").isEmpty()){
                    low24h = Double.parseDouble(csvRecord.get("low_24h"));
                }else{
                    low24h = 0;
                }if(!csvRecord.get("market_cap_change_percentage_24h").isEmpty()){
                    marketCapChangePer24h = Double.parseDouble(csvRecord.get("market_cap_change_percentage_24h"));
                }else{
                    marketCapChangePer24h = 0;
                }if(!csvRecord.get("price_change_24h").isEmpty()){
                    priceChange24h = Double.parseDouble(csvRecord.get("price_change_24h"));
                }else{
                    priceChange24h = 0;
                }if(!csvRecord.get("price_change_percentage_24h").isEmpty()){
                    priceChangePer24h = Double.parseDouble(csvRecord.get("price_change_percentage_24h"));
                }else{
                    priceChangePer24h = 0;
                }if(!csvRecord.get("market_cap_change_24h").isEmpty()){
                    marketCapChange24h = Double.parseDouble(csvRecord.get("market_cap_change_24h"));
                }else{
                    marketCapChange24h = 0;
                }if(!csvRecord.get("price").isEmpty()){
                    price = Double.parseDouble(csvRecord.get("price"));
                }else{
                    price = 0;
                }if(!csvRecord.get("rank").isEmpty()){
                    rank = Double.parseDouble(csvRecord.get("rank"));
                }else{
                    rank = 0;
                }if(!csvRecord.get("total_volume").isEmpty()){
                    totalVolume = Double.parseDouble(csvRecord.get("total_volume"));
                }else{
                    totalVolume = 0;
                }if(!csvRecord.get("market_cap").isEmpty()){
                    marketCap = Double.parseDouble(csvRecord.get("market_cap"));
                }else{
                    marketCap = 0;
                }if(!csvRecord.get("circulating_supply").isEmpty()){
                    circulatingSupply = Double.parseDouble(csvRecord.get("circulating_supply"));
                }else{
                    circulatingSupply = 0;
                }if(!csvRecord.get("atl").isEmpty()){
                    alt = Double.parseDouble(csvRecord.get("atl"));
                }else{
                    alt = 0;
                }if(!csvRecord.get("atl_change_percentage").isEmpty()){
                    atlChangePercentage = Double.parseDouble(csvRecord.get("atl_change_percentage"));
                }else{
                    atlChangePercentage = 0;
                }

                CryptoCurrencyMarketDataModel customer = new CryptoCurrencyMarketDataModel(
                        csvRecord.get("id"),
                        csvRecord.get("symbol"),
                        csvRecord.get("name"),
                        price,
                        marketCap,
                        totalVolume,
                        rank,
                        csvRecord.get("image"),
                        high24h,
                        low24h,
                        priceChange24h,
                        priceChangePer24h,
                        marketCapChange24h,
                        marketCapChangePer24h,
                        circulatingSupply,
                        totalSupply,
                        maxSupply,
                        alt,
                        atlChangePercentage,
                        csvRecord.get("atl_date"),
                        csvRecord.get("last_updated")
                );
                cryptoAndFiatModelArrayList.add(customer);
            }

        } catch (Exception e) {
            System.out.println("Reading CSV Error!");
            e.printStackTrace();
        } finally {
            try {
                assert fileReader != null;
                fileReader.close();
                assert csvParser != null;
                csvParser.close();
            } catch (IOException e) {
                System.out.println("Closing fileReader/csvParser Error!");
                e.printStackTrace();
            }
        }

        return cryptoAndFiatModelArrayList;
    }
}
