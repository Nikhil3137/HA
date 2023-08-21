import streamlit as st

def main():
    navigation_option = st.radio("Navigation", ["Home", "Results", "Analysis", "Examples", "Logs", "Verify", "Config"])

    if navigation_option == "Home":
        st.title('Home')
        st.write('This is the home page.')

    elif navigation_option == "Results":
        st.title('Results List')
        for item in range(25):
            st.write(f'Results {item}')

    elif navigation_option == "Analysis":
        st.title('Analysis')
        x, y = st.number_input('Input X'), st.number_input('Input Y')
        st.write('Result: ' + str(x + y))

    elif navigation_option == "Examples":
        st.title('Examples Menu')
        st.write('Select an example.')

    elif navigation_option == "Logs":
        st.title('View all of the logs')
        st.write('Here you may view all of the logs.')

    elif navigation_option == "Verify":
        st.title('Data verification is started...')
        st.write('Please stand by....')

    elif navigation_option == "Config":
        st.title('Configuration of the app.')
        st.write('Here you can configure the application')

if __name__ == "__main__":
    main()
