## Tarih işlemlerini yapabilmek için kullanılan kütüphane
import datetime

## Web arayüzü oluşturmak için kullanılan kütüphane
import streamlit as st

## Csv dosya işlemleri yapabilmek için kullanılan kütüphane
import pandas as pd

## Kendi olışturduğumuz kütüphaneyi içeri aktarıyoruz.
import order

## Csv dosyalarının okunması
df_pizza = pd.read_csv('pizza.csv')
df_sauce = pd.read_csv('sauce.csv')
df_orders = pd.read_csv('orders.csv')

st.markdown("<h1 style='text-align: center; color: grey;'>MENU</h1>", unsafe_allow_html=True)

## Pizza ve sos çeşitlerinin tablo olarak gösterilmesi
col1, col2 = st.columns(2)

with col1:
    st.table(df_pizza)

with col2:
    st.table(df_sauce)


## Kullanıcının seçmesi için input girdilerinin gösterilmesi
pizza = st.selectbox('Choose sauce, please!', df_pizza['Pizza'])

is_sauces = st.checkbox('Would you like to Sauce for your pizza')

## Sos seçmek isteniyorsa işletilecek kod blokları
if is_sauces:
    sauces = st.multiselect('Choose sauce, please!', df_sauce['Sauce'])

    ## Eğer sos seçilmiş ise seçilen pizza ve sosların fiyatlarını gösterir
    if len(sauces) != 0:
        receipt = order.Order(pizza, sauces).receipt()[0]
        price = order.Order(pizza, sauces).receipt()[1]
        st.json(receipt)

        st.warning(f'Total Price: {price} TL')

        ## İnput bilgilerini alınması
        FullName = st.text_input('Surname LastName')
        card_number = st.text_input('Card Number')

        ## Yapılan siparişin bilgilerinin csv dosyasına yazılması
        row = {'FullName':FullName, 'Pizza': pizza, 'Sauces': str(sauces), 'Price': price, 'CardNumber': card_number, 'Time': str(datetime.datetime.now())}
        df_orders.loc[len(df_orders.index)]= row

        if st.button('Sell'):        
            ## Csv dosyasının kayıt edilme işlemi
            df_orders.to_csv('orders.csv', index=False)

            ## Sipariş loglarının gösterilmesi
            st.write(df_orders)

## Sos seçmek istenmezse işletilecek kod blokları
else:
    receipt = order.Order(pizza).receipt()[0]
    st.json(receipt)
    
    ## İnput bilgilerini alınması
    FullName = st.text_input('Surname LastName')
    card_number = st.text_input('Card Number')
    
    if st.button('Sell'):
        price = order.Order(pizza).receipt()[1]

        ## Yapılan siparişin bilgilerinin csv dosyasına yazılması
        row = {'FullName':FullName, 'Pizza': pizza, 'Price': price, 'CardNumber': card_number, 'Time': str(datetime.datetime.now())}
        df_orders.loc[len(df_orders.index)]= row        
        
        ## Csv dosyasının kayıt edilme işlemi
        df_orders.to_csv('orders.csv', index=False)
        
        ## Sipariş loglarının gösterilmesi
        st.write(df_orders)


    
