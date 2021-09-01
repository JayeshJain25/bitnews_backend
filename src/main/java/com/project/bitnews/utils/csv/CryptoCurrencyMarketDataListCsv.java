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
                if(!csvRecord.get("total_supply").isEmpty()){
                    totalSupply = Double.parseDouble(csvRecord.get("total_supply"));
                }else{
                    totalSupply = 0;
                }
                if(!csvRecord.get("max_supply").isEmpty()){
                    maxSupply = Double.parseDouble(csvRecord.get("max_supply"));
                }else{
                    maxSupply = 0;
                }

                CryptoCurrencyMarketDataModel customer = new CryptoCurrencyMarketDataModel(
                        csvRecord.get("id"),
                        csvRecord.get("symbol"),
                        csvRecord.get("name"),
                        Double.parseDouble(csvRecord.get("price")),
                        Long.parseLong(csvRecord.get("market_cap")),
                        Long.parseLong(csvRecord.get("total_volume")),
                        Integer.parseInt(csvRecord.get("rank")),
                        csvRecord.get("image"),
                        Double.parseDouble(csvRecord.get("high_24h")),
                        Double.parseDouble(csvRecord.get("low_24h")),
                        Double.parseDouble(csvRecord.get("price_change_24h")),
                        Double.parseDouble(csvRecord.get("price_change_percentage_24h")),
                        Double.parseDouble(csvRecord.get("market_cap_change_24h")),
                        Double.parseDouble(csvRecord.get("market_cap_change_percentage_24h")),
                        Double.parseDouble(csvRecord.get("circulating_supply")),
                        totalSupply,
                        maxSupply,
                        Double.parseDouble(csvRecord.get("atl")),
                        Double.parseDouble(csvRecord.get("atl_change_percentage")),
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
