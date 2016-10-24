package com.example.zzz.usingjson;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        System.out.println(Data.JsonStr);

        //解析Json
        try {
            JSONObject jsonObject=new JSONObject(Data.JsonStr);
            JSONArray jsonArray=jsonObject.getJSONArray("arr");
            System.out.println(jsonArray);
            for(int i=0;i<jsonArray.length();i++){
                System.out.println(jsonArray.get(i));
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
