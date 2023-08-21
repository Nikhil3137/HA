import streamlit as st

def navigation():
    try:
        query_params = st.experimental_get_query_params()
        print("Query Params:", query_params)  # Print the query parameters
        path = query_params.get('p', [''])[0]  # Use .get() to safely retrieve the value
    except Exception as e:
        st.error('Error occurred:', e)
        return None
    return path

if __name__ == "__main__":
    path = navigation()

    if path == "home":
        st.title('Home')
        st.write('This is the home page.')

    elif path == "results":
        st.title('Results List')
        for item in range(25):
            st.write(f'Results {item}')

    elif path == "analysis":
        st.title('Analysis')
        x, y = st.number_input('Input X'), st.number_input('Input Y')
        st.write('Result: ' + str(x + y))

    elif path == "examples":
        st.title('Examples Menu')
        st.write('Select an example.')

    elif path == "logs":
        st.title('View all of the logs')
        st.write('Here you may view all of the logs.')

    elif path == "verify":
        st.title('Data verification is started...')
        st.write('Please stand by....')

    elif path == "config":
        st.title('Configuration of the app.')
        st.write('Here you can configure the application')
