# app.py
import streamlit as st
import time
from finance_team import finance_team
# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Fintelligence",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Page Title and Description ---
# --- Page Title and Description ---
st.markdown(f"<h1 style='color: #1407fa;'>💬 Multi-Agentic Financial Intelligence</h1>", unsafe_allow_html=True)

# --- Main Application Logic ---
def main():
    """
    Main function to run the Streamlit chatbot application.
    """
    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is your financial question?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                with st.spinner("Thinking..."): # Add spinner here
                    # Get response from the finance team
                    response = finance_team.run(message=prompt)
                    
                    # Process and display the response
                    if hasattr(response, 'content'):
                        full_response = response.content
                    elif isinstance(response, str):
                        full_response = response
                    else:
                        full_response = str(response)
                        
                    # Display the response with streaming effect
                    for i in range(0, len(full_response), 5):
                        message_placeholder.markdown(full_response[:i+5] + "▌")
                        time.sleep(0.01)  # Small delay for streaming effect
                    
                message_placeholder.markdown(full_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                full_response = "Sorry, I encountered an error while processing your request."

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()