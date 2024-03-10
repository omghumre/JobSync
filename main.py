import streamlit as st
import joblib
import re
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')

clf = joblib.load(open('clf.joblib','rb'))
tfidfd = joblib.load(open('tfidf.joblib','rb'))

def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText
def main():
    st.title("Find your dream Company")
    uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_feature = tfidfd.transform([cleaned_resume])
        prediction = clf.predict(input_feature)[0]
        # st.write(prediction)

        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction,"Unknown")
        st.write("Predicted Category:",category_name)

        df = pd.read_csv("companies.csv")
        # print(df.head())

        companies = df.loc[df['Job Title'] == category_name, 'Company'].values
        url = df.loc[df['Job Title'] == category_name, 'LI Job Post URL'].values
        for val in range(len(companies)):
            st.write(companies[val])
            st.link_button("Apply Now",url[val])

if __name__ == '__main__':
    main()
