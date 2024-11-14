import paho.mqtt.client as paho
import time
import streamlit as st
import json
values = 0.0
act1="ON"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="157.230.214.127"
port=1883
client1= paho.Client("alejandraPPalacios")
client1.on_message = on_message



st.title("Apagar luces")


if st.button('Apagar luces'):
    act1="apaga las luces"
    client1= paho.Client("alejandraPPalacios")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("vocesita", message)
    st.write("Las luces se han apagado")
else:
    st.write('')
    
if st.button('Prender luces'):
    act1="enciende las luces"
    client1= paho.Client("alejandraPPalacios")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("vocesita", message)
    st.write("Las luces se han prendido")
else:
    st.write('')

    
st.link_button("Volver a inicio", "https://finalinterfaces-fnfqrnjj9eidx5gwyv9uul.streamlit.app/")



