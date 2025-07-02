import streamlit as st
import groq
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement, qn
import io
import base64
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Resume & Cover Letter Writer",
    page_icon="📄",
    layout="wide"
)

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    try:
        client = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
        return client
    except Exception as e:
        st.error(f"Error initializing Groq client: {e}")
        return None

def generate_resume_content(client, user_data):
    """Generate resume content using Groq API"""
    prompt = f"""
    Create a professional resume for the following person. Format it as clean, structured text that can be easily converted to HTML:

    Personal Information:
    - Name: {user_data['name']}
    - Email: {user_data['email']}
    - Phone: {user_data['phone']}
    - Address: {user_data['address']}
    - LinkedIn: {user_data.get('linkedin', 'N/A')}

    Education: {user_data['education']}
    
    Work Experience: {user_data['work_experience']}
    
    Skills: {user_data['skills']}
    
    Target Job Role: {user_data['job_role']}
    
    Additional Information: {user_data.get('additional_info', 'None')}

    Please create a professional, ATS-friendly resume with clear sections. Include a professional summary at the top that highlights key qualifications for the target role.
    """
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating resume: {e}")
        return None

def generate_cover_letter(client, user_data, company_info):
    """Generate cover letter using Groq API"""
    prompt = f"""
    Write a professional cover letter for the following person applying to {company_info.get('company_name', 'the company')} for the position of {user_data['job_role']}.

    Applicant Information:
    - Name: {user_data['name']}
    - Target Role: {user_data['job_role']}
    - Work Experience: {user_data['work_experience']}
    - Skills: {user_data['skills']}
    - Education: {user_data['education']}

    Company Information:
    - Company Name: {company_info.get('company_name', 'Company')}
    - Job Description/Requirements: {company_info.get('job_description', 'Not provided')}
    - Hiring Manager: {company_info.get('hiring_manager', 'Hiring Manager')}

    Create a compelling, personalized cover letter that:
    1. Shows enthusiasm for the role and company
    2. Highlights relevant experience and skills
    3. Demonstrates knowledge of the company/role
    4. Has a professional tone
    5. Is concise but impactful
    
    Format it as a proper business letter.
    """
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1200
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating cover letter: {e}")
        return None

def create_resume_html(resume_content, user_data):
    """Convert resume content to HTML with styling"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f9f9f9;
            }}
            .resume-container {{
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                border-bottom: 3px solid #2c3e50;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            .name {{
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }}
            .contact-info {{
                font-size: 14px;
                color: #666;
                line-height: 1.4;
            }}
            .section {{
                margin-bottom: 25px;
            }}
            .section-title {{
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
                margin-bottom: 15px;
            }}
            .content {{
                white-space: pre-line;
                text-align: justify;
            }}
            @media print {{
                body {{ background-color: white; }}
                .resume-container {{ box-shadow: none; }}
            }}
        </style>
    </head>
    <body>
        <div class="resume-container">
            <div class="header">
                <div class="name">{user_data['name']}</div>
                <div class="contact-info">
                    {user_data['email']} | {user_data['phone']}<br>
                    {user_data['address']}
                    {f"<br>LinkedIn: {user_data['linkedin']}" if user_data.get('linkedin') else ""}
                </div>
            </div>
            <div class="content">{resume_content}</div>
        </div>
    </body>
    </html>
    """
    return html_content

def create_cover_letter_html(cover_letter_content, user_data):
    """Convert cover letter to HTML with styling"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f9f9f9;
            }}
            .letter-container {{
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: right;
                margin-bottom: 30px;
            }}
            .sender-info {{
                font-size: 14px;
                color: #666;
                line-height: 1.4;
            }}
            .date {{
                margin: 20px 0;
                font-size: 14px;
            }}
            .content {{
                white-space: pre-line;
                text-align: justify;
                font-size: 14px;
                line-height: 1.6;
            }}
            @media print {{
                body {{ background-color: white; }}
                .letter-container {{ box-shadow: none; }}
            }}
        </style>
    </head>
    <body>
        <div class="letter-container">
            <div class="header">
                <div class="sender-info">
                    {user_data['name']}<br>
                    {user_data['email']}<br>
                    {user_data['phone']}<br>
                    {user_data['address']}
                </div>
            </div>
            <div class="date">{datetime.now().strftime('%B %d, %Y')}</div>
            <div class="content">{cover_letter_content}</div>
        </div>
    </body>
    </html>
    """
    return html_content

def create_docx_resume(resume_content, user_data):
    """Create a Word document for the resume"""
    doc = Document()
    
    # Header
    header = doc.sections[0].header
    header_para = header.paragraphs[0]
    header_para.text = f"{user_data['name']} | {user_data['email']} | {user_data['phone']}"
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Title
    title = doc.add_heading(user_data['name'], 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Contact info
    contact_para = doc.add_paragraph()
    contact_para.add_run(f"{user_data['email']} | {user_data['phone']}\n{user_data['address']}")
    contact_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Add a line break
    doc.add_paragraph()
    
    # Resume content
    doc.add_paragraph(resume_content)
    
    # Save to bytes
    docx_buffer = io.BytesIO()
    doc.save(docx_buffer)
    docx_buffer.seek(0)
    return docx_buffer

def create_docx_cover_letter(cover_letter_content, user_data):
    """Create a Word document for the cover letter"""
    doc = Document()
    
    # Header with contact info
    header_para = doc.add_paragraph()
    header_para.add_run(f"{user_data['name']}\n{user_data['email']}\n{user_data['phone']}\n{user_data['address']}")
    header_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    # Add date
    date_para = doc.add_paragraph()
    date_para.add_run(datetime.now().strftime('%B %d, %Y'))
    date_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Add a line break
    doc.add_paragraph()
    
    # Cover letter content
    doc.add_paragraph(cover_letter_content)
    
    # Save to bytes
    docx_buffer = io.BytesIO()
    doc.save(docx_buffer)
    docx_buffer.seek(0)
    return docx_buffer

def main():
    st.title("🎯 AI Resume & Cover Letter Writer")
    st.markdown("Create professional resumes and cover letters tailored to your target job role.")
    
    # Initialize Groq client
    client = get_groq_client()
    if not client:
        st.stop()
    
    # Sidebar for user inputs
    st.sidebar.header("📋 Your Information")
    
    # Personal Information
    st.sidebar.subheader("Personal Details")
    name = st.sidebar.text_input("Full Name*", placeholder="John Doe")
    email = st.sidebar.text_input("Email*", placeholder="john.doe@email.com")
    phone = st.sidebar.text_input("Phone*", placeholder="+1 (555) 123-4567")
    address = st.sidebar.text_area("Address*", placeholder="123 Main St, City, State 12345")
    linkedin = st.sidebar.text_input("LinkedIn Profile (optional)", placeholder="https://linkedin.com/in/johndoe")
    
    # Professional Information
    st.sidebar.subheader("Professional Information")
    job_role = st.sidebar.text_input("Target Job Role*", placeholder="Software Developer")
    education = st.sidebar.text_area("Education*", placeholder="Bachelor's in Computer Science, XYZ University (2020)")
    work_experience = st.sidebar.text_area("Work Experience*", placeholder="Software Engineer at ABC Corp (2020-2023)\n- Developed web applications\n- Led team of 3 developers")
    skills = st.sidebar.text_area("Skills*", placeholder="Python, JavaScript, React, SQL, Git")
    additional_info = st.sidebar.text_area("Additional Information (optional)", placeholder="Certifications, Projects, Awards, etc.")
    
    # Company-specific information for cover letter
    st.sidebar.subheader("Cover Letter Details")
    company_name = st.sidebar.text_input("Company Name", placeholder="Tech Corp Inc.")
    hiring_manager = st.sidebar.text_input("Hiring Manager Name (optional)", placeholder="Ms. Jane Smith")
    job_description = st.sidebar.text_area("Job Description/Requirements (optional)", placeholder="Paste job posting details here...")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📄 Resume")
        if st.button("Generate Resume", type="primary", use_container_width=True):
            if not all([name, email, phone, address, job_role, education, work_experience, skills]):
                st.error("Please fill in all required fields marked with *")
            else:
                with st.spinner("Generating your professional resume..."):
                    user_data = {
                        'name': name,
                        'email': email,
                        'phone': phone,
                        'address': address,
                        'linkedin': linkedin,
                        'job_role': job_role,
                        'education': education,
                        'work_experience': work_experience,
                        'skills': skills,
                        'additional_info': additional_info
                    }
                    
                    resume_content = generate_resume_content(client, user_data)
                    if resume_content:
                        st.session_state['resume_content'] = resume_content
                        st.session_state['user_data'] = user_data
                        st.success("Resume generated successfully!")
        
        # Display resume if generated
        if 'resume_content' in st.session_state:
            st.subheader("📋 Resume Preview")
            resume_html = create_resume_html(st.session_state['resume_content'], st.session_state['user_data'])
            st.components.v1.html(resume_html, height=800, scrolling=True)
            
            # Download button for resume
            resume_docx = create_docx_resume(st.session_state['resume_content'], st.session_state['user_data'])
            st.download_button(
                label="📥 Download Resume (.docx)",
                data=resume_docx.getvalue(),
                file_name=f"{st.session_state['user_data']['name']}_Resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
    
    with col2:
        st.header("✉️ Cover Letter")
        if st.button("Generate Cover Letter", type="primary", use_container_width=True):
            if not all([name, email, phone, address, job_role, education, work_experience, skills]):
                st.error("Please fill in all required fields marked with *")
            elif not company_name:
                st.error("Please enter the company name for the cover letter")
            else:
                with st.spinner("Crafting your personalized cover letter..."):
                    user_data = {
                        'name': name,
                        'email': email,
                        'phone': phone,
                        'address': address,
                        'linkedin': linkedin,
                        'job_role': job_role,
                        'education': education,
                        'work_experience': work_experience,
                        'skills': skills,
                        'additional_info': additional_info
                    }
                    
                    company_info = {
                        'company_name': company_name,
                        'hiring_manager': hiring_manager,
                        'job_description': job_description
                    }
                    
                    cover_letter_content = generate_cover_letter(client, user_data, company_info)
                    if cover_letter_content:
                        st.session_state['cover_letter_content'] = cover_letter_content
                        st.session_state['user_data'] = user_data
                        st.success("Cover letter generated successfully!")
        
        # Display cover letter if generated
        if 'cover_letter_content' in st.session_state:
            st.subheader("📝 Cover Letter Preview")
            cover_letter_html = create_cover_letter_html(st.session_state['cover_letter_content'], st.session_state['user_data'])
            st.components.v1.html(cover_letter_html, height=800, scrolling=True)
            
            # Download button for cover letter
            cover_letter_docx = create_docx_cover_letter(st.session_state['cover_letter_content'], st.session_state['user_data'])
            st.download_button(
                label="📥 Download Cover Letter (.docx)",
                data=cover_letter_docx.getvalue(),
                file_name=f"{st.session_state['user_data']['name']}_Cover_Letter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
    
    # Footer
    st.markdown("---")
    st.markdown("💡 **Tips for better results:**")
    st.markdown("- Provide detailed work experience with specific achievements")
    st.markdown("- Include relevant skills for your target job role")
    st.markdown("- Add company-specific information for personalized cover letters")
    st.markdown("- Review and customize the generated content before using")

if __name__ == "__main__":
    main()
