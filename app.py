import paho.mqtt.client as paho
import time
import streamlit as st
import json
values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("alejandraPPalacios")
client1.on_message = on_message



st.title("Cerrar garaje")

if st.button('Cerrar garaje'):
    act1="ON"
    client1= paho.Client("alejandraPPalacios")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("maluma_s", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Detener la puerta'):
    act1="OFF"
    client1= paho.Client("alejandraPPalacios")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("maluma_s", message)
  
    

    
st.link_button("Volver a inicio", "https://finalinterfaces-fnfqrnjj9eidx5gwyv9uul.streamlit.app/")



