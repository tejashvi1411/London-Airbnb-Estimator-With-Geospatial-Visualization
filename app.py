import streamlit as st 
import joblib
import pandas as pd
import pickle
from tensorflow.keras.models import load_model
import numpy as np
from streamlit_folium import folium_static
import folium
model=load_model('londonmodel.h5')


def main():
	"""London Airbnb Price Estimation With Geospatial Analysis"""
	st.subheader("A Project By Tejashvi")
	html_temp = """
	<div style="background-color:black;padding:20px">
	<h3 style="color:white;text-align:center;">London Airbnb Price Estimation With Geospatial Analysis </h3>
	</div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	activity = ['About','Prediction','Glimpse Of Geospatial Analysis']
	choice = st.sidebar.selectbox("Please Click Here To Navigate The Web App",activity)

	if choice == 'About':
		st.markdown("<h3 style='text-align: center; color: black;'>The Web App Estimates Airbnb Prices For The City Of london</h3>", unsafe_allow_html=True)
		st.markdown("<h4 style='text-align: center; color: red;'>A Glimpse Of Geospatial Analysis Can Also Be Checked Out!</h4>", unsafe_allow_html=True)
	
	if choice == 'Glimpse Of Geospatial Analysis':
		st.info("Just A Small Glimpse Of Geospatial Analysis Where Some Of The Costliest Airbnbs Are Plotted Along With The Famous Hyde Park")
		st.info("Find The Indepth Geospatial Analysis On The Github Repository Of This Project")
		df=pd.read_csv("LondonAirbnbUpdated.csv")
		m = folium.Map(location=[51.508610,  -0.163611], zoom_start=12)
		tooltip = "Hyde Park"
		folium.Marker([51.508610, -0.163611], popup="Hyde Park",icon=folium.Icon(color="red", icon="info-sign"), tooltip=tooltip).add_to(m)
		for i in range(len(df)):
			if df["price"].iloc[i]>=950:
				folium.Marker([df['latitude'].iloc[i], df['longitude'].iloc[i]]).add_to(m)
		folium_static(m)
		st.info("Hyde Park And Some Of The Most Expensive London Airbnbs")

	if choice == 'Prediction':
		st.info("Fill In The Credentials")
	
		nhood=['Lambeth', 'Islington', 'Kensington and Chelsea','Hammersmith and Fulham', 'Barnet', 'Hounslow','Richmond upon Thames', 'Haringey', 'Southwark', 'Croydon','Westminster', 'Waltham Forest', 'Brent', 'Camden', 'Newham','Tower Hamlets', 'Redbridge', 'Hackney', 'Merton', 'Lewisham','Wandsworth', 'Bromley', 'Havering', 'Greenwich', 'Ealing','Enfield', 'City of London', 'Barking and Dagenham', 'Hillingdon','Harrow', 'Kingston upon Thames', 'Bexley', 'Sutton']
		neighbourhood_cleansed = st.selectbox("Select Preferred London Neighbourhood", nhood)
		if neighbourhood_cleansed=="Lambeth":
			neighbourhood_cleansed=72.561446
		elif neighbourhood_cleansed=="Islington":
			neighbourhood_cleansed=80.465409	
		elif neighbourhood_cleansed=="Kensington and Chelsea":
			neighbourhood_cleansed=102.767814
		elif neighbourhood_cleansed=="Hammersmith and Fulham":
			neighbourhood_cleansed=83.420979
		elif neighbourhood_cleansed=="Barnet":
			neighbourhood_cleansed=65.437122
		elif neighbourhood_cleansed=="Hounslow":
			neighbourhood_cleansed=68.097561
		elif neighbourhood_cleansed=="Richmond upon Thames":
			neighbourhood_cleansed=83.728637
		elif neighbourhood_cleansed=="Haringey":
			neighbourhood_cleansed=60.783742
		elif neighbourhood_cleansed=="Southwark":
			neighbourhood_cleansed=74.907508
		elif neighbourhood_cleansed=="Croydon":
			neighbourhood_cleansed=53.240367	
		elif neighbourhood_cleansed=="Westminster":
			neighbourhood_cleansed=98.121761
		elif neighbourhood_cleansed=="Waltham Forest":
			neighbourhood_cleansed=60.879499 
		elif neighbourhood_cleansed=="Brent":
			neighbourhood_cleansed=68.665965
		elif neighbourhood_cleansed=="Camden":
			neighbourhood_cleansed=86.634433
		elif neighbourhood_cleansed=="Newham":
			neighbourhood_cleansed=63.208386
		elif neighbourhood_cleansed=="Tower Hamlets":
			neighbourhood_cleansed=71.733002
		elif neighbourhood_cleansed=="Redbridge":
			neighbourhood_cleansed=53.594761
		elif neighbourhood_cleansed=="Hackney":
			neighbourhood_cleansed=73.768269	
		elif neighbourhood_cleansed=="Merton":
			neighbourhood_cleansed=72.905222
		elif neighbourhood_cleansed=="Lewisham":
			neighbourhood_cleansed=59.708689
		elif neighbourhood_cleansed=="Wandsworth":
			neighbourhood_cleansed=81.092986
		elif neighbourhood_cleansed=="Bromley":
			neighbourhood_cleansed=61.988743
		elif neighbourhood_cleansed=="Havering":
			neighbourhood_cleansed=66.390756
		elif neighbourhood_cleansed=="Greenwich":
			neighbourhood_cleansed=71.494956
		elif neighbourhood_cleansed=="Ealing":
			neighbourhood_cleansed=63.396774 
		elif neighbourhood_cleansed=="Enfield":
			neighbourhood_cleansed=59.059423
		elif neighbourhood_cleansed=="City of London":
			neighbourhood_cleansed=113.377907
		elif neighbourhood_cleansed=="Barking and Dagenham":
			neighbourhood_cleansed=54.794805
		elif neighbourhood_cleansed=="Hillingdon":
			neighbourhood_cleansed=61.129952
		elif neighbourhood_cleansed=="Harrow":
			neighbourhood_cleansed=59.174713
		elif neighbourhood_cleansed=="Kingston upon Thames":
			neighbourhood_cleansed=64.633947
		elif neighbourhood_cleansed=="Bexley":
			neighbourhood_cleansed=51.232143
		elif neighbourhood_cleansed=="Sutton":
			neighbourhood_cleansed=55.112211
		
		accommodates = st.slider("Select Accommodation Capacity Of Airbnb",1,10,1)
		
		bedrooms = st.slider("Select Number Of Bedrooms",1,10,1) 
		beds = st.slider("Select Number Of Beds",1,10,1) 
		calculated_host_listings_count = st.slider("Select Number Of Listings By Host",1,10,1) 
		bathrooms = st.slider("Select Number Of Bathrooms",1,8,1) 
		
		roomtype=["Entire Home Or Apartment","Private Room","Shared Room","Hotel Room"]
		room_type = st.selectbox("Select Type Of Room/House",roomtype)
		if room_type=="Entire Home Or Apartment":
			room_type=104.354432
		elif room_type=="Private Room":
			room_type=48.795135
		elif room_type=="Shared Room":
			room_type=58.486486
		elif room_type=="Hotel Room":
			room_type=91.94086022


		x=[neighbourhood_cleansed,room_type,accommodates,bedrooms,beds,calculated_host_listings_count,bathrooms]
		s = np.load('std.npy')
		m = np.load('mean.npy')
		y=((np.array(x) - m)) / s 
		z=[]
		for i in y:
			z.append(i)
		if st.button("Predict"):
			prediction = model.predict([z])			
			final_result = prediction
			st.success("Price: {}".format(final_result))
if __name__ == '__main__':
	main()
