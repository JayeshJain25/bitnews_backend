package com.project.bitnews.utils.csv;

import com.project.bitnews.mongo.model.CryptoAndFiatModel;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class CryptoCurrencyListCsv {

    public static List<CryptoAndFiatModel> parseCsvFile(InputStream is) {
        BufferedReader fileReader = null;
        CSVParser csvParser = null;

        List<CryptoAndFiatModel> cryptoAndFiatModelArrayList = new ArrayList<>();

        try {
            fileReader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            csvParser = new CSVParser(fileReader,
                    CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());

            Iterable<CSVRecord> csvRecords = csvParser.getRecords();

            for (CSVRecord csvRecord : csvRecords) {

                double price;
                double marketCap;
                double totalVolume;
                double rank;

                if(!csvRecord.get("price").isEmpty()){
                    price = Double.parseDouble(csvRecord.get("price"));
                }else{
                    price = 0;
                }
                if(!csvRecord.get("market_cap").isEmpty()){
                    marketCap = Double.parseDouble(csvRecord.get("market_cap"));
                }else{
                    marketCap = 0;
                }if(!csvRecord.get("total_volume").isEmpty()){
                    totalVolume = Double.parseDouble(csvRecord.get("total_volume"));
                }else{
                    totalVolume = 0;
                }
                if(!csvRecord.get("rank").isEmpty()){
                    rank = Double.parseDouble(csvRecord.get("rank"));
                }else{
                    rank = 0;
                }

                CryptoAndFiatModel customer = new CryptoAndFiatModel(
                        csvRecord.get("id"),
                        csvRecord.get("symbol"),
                        csvRecord.get("name"),
                        price,
                        marketCap,
                        totalVolume,
                        rank,
                        csvRecord.get("image"),csvRecord.get("type"));
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
