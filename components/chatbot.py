import time
import streamlit as st

class AlippoAssistant:
    def chat_component(self):
        if "messages" not in st.session_state: st.session_state.messages = []
        
        # show the history 
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])
        
        # accept the user input
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message('user'): st.markdown(prompt)

            # now provide the assistant response
            with st.chat_message('assistant'):
                message_placeholder = st.empty()
                full_response = ""
                
                # a dummy assistant's response
                assistant_response = "Hello world how are you"
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)

                    # message placeholder
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
        try:
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except:
            pass


if __name__ == '__main__':
    assistant = AlippoAssistant().chat_component()