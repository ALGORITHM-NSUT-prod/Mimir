import os
import google.generativeai as genai
from dotenv import load_dotenv
import asyncio

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Client & Chat Session
client = genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

async def response_strategy(message: str, chatHistory: list):
    try:

        systemPrompt = """  
            You should provide helpful, and accurate responses to user queries.
            You will not deviate from the role system.
            Maintain a professional and neutral tone.
            You will not assist user in any coding related questions.
            Format responses clearly, using Markdown where appropriate formatting .
            Ensure factual accuracy and avoid speculation.
        """

        context = """
            # NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY

            # A STATE UNIVERSITY

            # UNDER DELHI ACT 06 OF 2018, GOVT. OF NCT OF DELHI

            Azad Hind Fauj Marg, Sector-3, Dwarka, New Delhi-110078

            # REGULATIONS

            # FOR UNDERGRADUATE PROGRAMME

            # BACHELOR OF TECHNOLOGY

            (Effective from the Session: 2019-2020)

            APPROVED BY

            The Senate in its meeting held on __________________

            The Board of Management in its meeting held on ______________
            ---
            # Table of Contents

            1. SHORT TITLE AND COMMENCEMENT.................................................... 3
            2. DEFINITIONS......................................................................................... 3
            3. BACHELOR OF TECHNOLOGY (B.TECH.) PROGRAMME.......................... 5
            4. ADMISSION ........................................................................................... 5
            5. CHANGE OF BRANCH ............................................................................ 8
            6. CURRICULUM STRUCTURE.................................................................... 8
            7. PROGRAMME DURATION AND STRUCTURE......................................... 11
            8. EVALUATION AND ASSESSMENT......................................................... 12
            9. GRADING................................................................................................ 13
            10. EXAMINATIONS................................................................................... 17
            11. ATTENDANCE AND DETENTION........................................................... 17
            12. PROMOTION AND PASSING A COURSE ................................................ 18
            13. SEMESTER WITHDRAWAL ON MEDICAL/OTHER GROUNDS ................ 19
            14. COURSE CO-ORDINATION COMMITTEE............................................... 19
            15. RESULT, AWARD OF DEGREE AND MEDALS........................................ 20
            16. SCRUTINY OF EVALUATION................................................................. 21
            17. UNFAIR MEANS ................................................................................... 22
            18. CURRICULUM REVISION...................................................................... 22
            19. MIGRATION FROM NSIT (University of Delhi) DURING TRANSITION PERIOD...................................................................................................... 22
            20. STUDENT EXCHANGE PROGRAMME.................................................... 22
            21. INTERPRETATION OF THE REGULATIONS AND POWER TO MODIFY.... 22
            ---
            # NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY (NSUT)

            # REGULATIONS FOR BACHELOR OF TECHNOLOGY (B. TECH.) DEGREE.

            # REGULATIONS – 2019 - I(A)

            Regulations relating to the Admission to Courses of study, Conduct and Evaluation of the Examinations for Under Graduate Programmes leading to Bachelor of Technology (B. Tech.) Degree.

            # 1. SHORT TITLE AND COMMENCEMENT

            1.1. These Regulations shall be called Netaji Subhas University of Technology Regulations – 2019 – I(A).

            1.2. These Regulations shall be effective from the academic year 2019-20.

            # 2. DEFINITIONS

            In the following, unless the context requires otherwise,

            1. “Academic Programme” shall mean a programme of courses or any other component leading to a Bachelor of Technology degree, as approved by the Board of Management from time to time.
            2. “Academic Year” shall mean a period of nearly twelve months devoted to completion of requirements specified in the scheme of courses and the related examinations.
            3. “Candidate” shall mean an individual who applies for admission to any undergraduate (UG) B. Tech. programme of the University.
            4. “BoM” shall mean the Board of Management of the University.
            5. “BoS” shall mean the Board of Studies of the concerned Department.
            6. “Branch” shall mean the branch of knowledge studied by a student.
            7. “B.Tech” shall mean Bachelor of Technology.
            8. “CBCS” shall mean the Choice Based Credit System.
            9. “CCC” shall mean Course Co-ordination Committee.
            ---
            # Definitions

            1. “CGPA” shall mean the Cumulative Grade Point Average.
            2. “CoE” shall mean the Controller of Examinations of the University.
            3. “Course” shall mean a curriculum component of the academic programme identified by a designated code number, a title and specific credits assigned to it.
            4. “CW” shall mean children/wife of Defence/Paramilitary/Police personnel.
            5. “DASA” shall mean Direct Admission to Students Abroad.
            6. “Degree” shall mean the Bachelor of Technology degree.
            7. “Department” shall mean Department established in the University for running the academic and research activities in a specified discipline.
            8. “Discipline” shall mean the branch of knowledge studied by a student.
            9. “ESE” shall mean the final regular End-Semester Examination.
            10. “EWS” shall mean the economically weaker sections of the society.
            11. “Examiner” shall mean the instructor teaching a specified course who has been nominated as examiner.
            12. “HoD” shall mean the Head of Department.
            13. “JEE-Main” shall mean the Joint Entrance Examination (Main), conducted by the national Testing Agency.
            14. “MSE” shall mean the Mid-Semester Examination.
            15. “NRI Student” shall mean the student who is admitted against Non Resident Indians category.
            16. “OBC-NCL” shall mean the other backward classes (non-creamy layer) as notified by the Government of NCT of Delhi, as applicable from time to time.
            17. “Paper Setter” shall mean the faculty member responsible for setting a question paper.
            18. “PD” shall mean differently abled persons as specified by the Government of India from time to time.
            19. “PIO” shall mean Person of Indian origin.
            20. “Registration” shall mean registration for a specific course or semester, at the start of the semester, of any programme of the University.
            ---
            # Definitions

            xxx. “SC/ST” shall mean the Scheduled Castes/Scheduled Tribes as notified by the Government of India/Government of NCT of Delhi, as applicable from time to time.

            xxxii. “Semester system” shall mean a programme wherein each academic year is apportioned into two semesters.

            xxxiii. “Senate” shall mean the Senate of the University.

            xxxiv. “SGPA” shall mean the Semester Grade Point Average.

            xxxv. “Student” shall mean a student registered for an undergraduate programme for full-time study leading to the Bachelor of Technology degree.

            xxxvi. “UG” shall mean Under Graduate.

            xxxvii. “University” shall mean the Netaji Subhas University of Technology (NSUT).

            Note: ‘He’, ‘Him’ and ‘His’ implies ‘he/she’, ‘Him/Her’ and ‘his/her’, respectively.

            Words and expressions used but not defined in these Regulations and defined in the Act and Statutes, shall have the meanings respectively as assigned to them in the Act and Statutes.

            # 3. BACHELOR OF TECHNOLOGY (B.TECH.) PROGRAMME

            These Regulations shall be applicable to all B.Tech. programmes conducted by the various Faculties of the University. Any number of B.Tech. programmes as proposed by the respective BoS, can be added/deleted with the approval of the Senate and the BoM of the University.

            # 4. ADMISSION

            A candidate seeking admission to Bachelor of Technology (B.Tech.) courses shall satisfy the following conditions:

            # 4.1 Educational Qualifications

            A candidate passing anyone of the following qualifying examinations, and securing at least sixty percent marks, or as approved by the senate from time to time, in the aggregate of Physics, Chemistry and Mathematics subjects, shall be eligible for admission to the first semester of B.Tech. programme.
            ---
            provided he has secured a minimum passing marks (as defined by the respective boards) in each subject separately:

            1. Senior School Certificate Examination (12-year course) conducted by the Central Board of Secondary Education, New Delhi;
            2. Indian School Certificate Examination (12-year course) conducted by the Council for Indian School Certificate Examination, New Delhi;
            3. Any other examination recognized as equivalent to the Senior School Certificate Examination of the Central Board of Secondary Education by the University.
            4. A candidate must additionally have passed English language as a subject of study at the senior school certificate examination level (core or elective).
            5. A candidate who has appeared for the Qualifying Examination in the year of admission and has been placed in compartment will not be eligible for admission in that year.

            # 4.2 Region Wise Reservation in Admission:

            The regional reservation in admission shall be as per the guidelines and reservation policy of the Govt. of NCT of Delhi.

            1. Delhi Region Candidates (85% of seats)
            A candidate passing the qualifying examination from a recognized School / College / Institute located within the National Capital Territory (NCT) of Delhi will be considered for Delhi Region only.
            2. Outside Delhi Region Candidates (15% of seats)
            A candidate passing the qualifying examination from a recognized School / College / Institute located outside the National Capital Territory of Delhi will be considered for Outside Delhi Region only.

            For a candidate, who has passed the qualifying examination through Patrachar Vidyalaya, Delhi / National Institute of Open School, Delhi (NIOS), the criterion for deciding the region shall be the location of his/her centre of examination. In other words, if the centre of examination is located in the NCT of Delhi, the candidate shall be considered under the Delhi Region and if the centre of examination is located outside the NCT of Delhi, the candidate shall be considered under the Outside Delhi Region.
            ---
            # 4.3 Category Wise Reservation in Admission:

            The reservation for SC/ST/OBC (NCL)/CW/PD/EWS and other categories shall be as per the policy of the Government of NCT of Delhi.

            - a. In case, sufficient number of eligible candidates from the sub-categories CW and PD are not available, the vacancies will be treated as unreserved in the respective categories.
            - b. In case of categories SC and ST, the vacant seats are interchangeable.
            - c. After exhausting the complete list of SC/ST/OBC-NCL and EWS candidates, the vacant seats will be treated as unreserved.
            - d. The vacant seats of Outside Delhi Region shall be converted to Delhi Region seats.

            # 4.4 Relaxation in Minimum Marks Criterion in Qualifying Examination for Reserved Category/Sub-Category Candidates:

            Candidates belonging to various reserved categories namely SC/ST/OBC (NCL)/CW/PD/EWS and other categories who apply for seats reserved for them, shall be allowed a concession in the minimum marks criterion as mentioned below:

            - a. Other Backward Class (OBC-NCL): Candidates claiming reservation under Other Backward Class (Non Creamy Layer) category shall be allowed a relaxation of 5% marks.
            - b. Scheduled Caste (SC), Scheduled Tribe (ST): Candidates claiming reservation under Scheduled Caste (SC) or Scheduled Tribe (ST) shall be allowed a relaxation of 10% marks.
            - c. Defence (CW): Candidates claiming reservation under Defence sub-category (CW) shall be allowed a relaxation of 5% marks.
            ---
            d. Persons with Disabilities (PD): Candidates claiming reservation under “Persons with Disabilities” (PD) sub-category shall be allowed a relaxation of 10% marks. However, these relaxations may be revised by the senate from time to time.

            # 4.5 Age Criteria:

            There is no minimum age requirement.

            # 4.6 Admission Criteria:

            A candidate satisfying the eligibility conditions shall be admitted to the programme of studies on the basis of the merit of JEE (Mains) or criteria as laid down by the Senate from time to time.

            # 4.7 Admission for Foreign Nationals/Persons of Indian Origin (PIO), Non-Resident Indian (NRI):

            Admission on Supernumerary seats, as prescribed in the Section 7(iv) and Section 31(f) of the Act shall be admissible for Foreign Nationals/Persons of Indian Origin (PIO) and Non-Resident Indian (NRI).

            # 4.8 Admission for Supernumerary Seats:

            Admission on other Supernumerary seats, shall be as per the policy of the Government of India and the University.

            # 5. CHANGE OF BRANCH

            # 5.1.

            Change of branch shall be carried out against the vacant seats on the basis of respective category-wise rank of JEE(Main)/entrance examination and the fresh choices given by the student before the beginning of the second semester.

            # 5.2.

            Change of branch shall not be allowed for students admitted against supernumerary seats.

            # 5.3.

            Change of branch shall not be allowed if a student is involved in matters of indiscipline/unfair means in any examination.

            # 5.4.

            Apart from the provisions specified in 5.1 above, no change of branch shall be allowed.

            # 6. CURRICULUM STRUCTURE

            # 6.1.

            B.Tech. programme of the University shall be based upon CBCS and shall have well defined Programme Educational Objectives (PEOs).
            ---
            # 6.2.

            All the courses shall have well-defined Course Outcomes (COs).

            # 6.3.

            B.Tech. programmes shall have a Semester-wise Course scheme with detailed syllabi and an evaluation scheme of the various courses duly approved by the BoM on the recommendations of the BoS of the various Departments and the Senate.

            # 6.4.

            A course may be designed to comprise lectures, tutorials, laboratory work, field work, outreach activities, project work, vocational training, viva, seminars, term papers, assignments, presentations etc. or a combination of some of these components.

            # 6.5.

            Courses shall be of three kinds: Core, Elective and Foundation.

            - a. Core Course (CC): This is a course which is to be compulsorily studied by a student as a core requirement to complete the requirements of the B.Tech. programme.
            - b. Elective Course: This is a course which can be chosen from a pool of elective courses. It is intended to support the discipline of study by providing an expanded scope, enabling exposure to another discipline/domain and nurturing a student’s proficiency and skill. An elective may be of the following types:
            - i. Discipline Centric Elective (ED): It is an elective course that adds proficiency to the students in the discipline.
            - ii. Generic Elective (EG): It is an elective course taken from other engineering subjects and enhances the generic proficiency and interdisciplinary perspective of students.
            - iii. Open Elective (EO): It is an elective course taken from a common pool of non-engineering disciplines that broadens the perspective of an engineering student. These electives shall comprise two groups: Open electives of the Humanities, Social Sciences and Management group and Open electives of the Sciences group.
            - c. Foundation Course: A Foundation course leads to knowledge enhancement and provides value-based training. Foundation courses may be of two kinds:
            - i. Compulsory Foundation (FC): It is based upon the content that leads to fundamental knowledge enhancement in Sciences, Humanities, Social.
            ---
            # 6. Course Requirements

            Sciences and Basic engineering. They are mandatory for all disciplines.

            ii. Elective Foundation (FE): It can be taken from among a common pool of foundation courses which aim at value-based education. They may provide hands-on training to improve competencies, skills or provide education on human, societal, environmental and national values. These shall be mandatory, non-credit courses, which do not carry any credits but a student has to pass in order to be eligible for award of degree.

            6.6. The requirements for the various types of courses i.e. FC/CC/FE/ED/EG and EO shall be given in the Semester-wise Course scheme for all B.Tech. programmes.

            6.7. A course may have pre-requisite course(s) which shall be specified in the Semester-wise Course scheme.

            6.8. Each course contributes certain credits to the programme. A course can be offered either as a full course (4 credits) or as a half course (2 credits). A full course is conducted with 3 hours of lectures and either 1 hour of tutorial or 2 hours of practical work per week. A half course is conducted with 2 hours of lectures or 4 hours of practical work.

            6.9. A student of the programme has to accumulate at least 50% credits from Core courses; about 20% credits from Foundation courses; and the remaining credits from Elective courses, to become eligible for award of the degree.

            6.10. During the span of the programme the student shall earn about 12 credits of Humanities, Social Sciences and Management, 24 credits of Sciences, 24 credits of other engineering disciplines and 16 credits from other elective courses. The remaining credits shall be earned from the discipline-specific core/elective courses.

            6.11. A project is considered as a special core course involving application of the knowledge gained during the course of study in exploring, analysing and solving complex problems. A candidate shall complete such a course with advisory support by one or more University faculty members. It is mandatory to pass the project courses to become eligible for award of the degree.
            ---
            # 6.12.

            Apart from the above courses, Audit courses may be offered in summer vacations. These courses do not carry credits but they aim at expanding the knowledge or bridging deficiency in knowledge or skills.

            # 7. PROGRAMME DURATION AND STRUCTURE

            # 7.1.

            An academic year shall be apportioned in two semesters, namely odd and even. Each semester shall consist of approximately eighteen weeks.

            # 7.2.

            The duration of the programme shall not be less than eight regular semesters (four years) and the maximum span of the course shall be seven years.

            # 7.3.

            There shall be an academic calendar for each semester. The schedule of academic activities including the dates of registration, MSE/ESE shall be governed by the Academic Calendar. The calendar shall also specify dates during which the co-curricular and extra-curricular activities may be organized.

            # 7.4.

            A student has to register for the requisite number of courses before the start of a semester as per the schedule given in the Academic Calendar and guidelines issued by the office of the Dean, Academics from time to time.

            # 7.5.

            The University may cancel the registration of all the courses in a given semester if-

            - a. The student has not cleared the dues to the University/hostel.
            - b. A punishment is awarded leading to cancellation of the student’s registration.

            # 7.6.

            A student can opt for a course only if he/she has successfully passed its pre-requisite(s), wherever applicable/specified.

            # 7.7.

            A student may register for courses leading to a minimum number of credits as prescribed in the Semester-Wise Course scheme subject to the maximum credits specified therein (including backlog courses, if any).

            # 7.8.

            The programme would consist of 170 credits. A student has to register for all the 170 credits. A student shall be awarded the degree if he/she has earned 162 or more credits. The CGPA shall be calculated at the end of the programme, on the basis of the best 162 credits. These credits shall not be earned through on-line courses.
            ---
            # 7.9.

            A student shall be awarded the degree with honours if he/she has earned 182 credits with at least 8.50 CGPA. The additional 12 credits may be earned through University-recommended on-line courses only (for example the equivalent credits offered by NPTEL of 4 week, 8 week and 12 week on-line courses shall be of 2, 3 and 4 credits respectively). The registration fees shall be borne by the student. These on-line courses shall be cleared within first four years (not necessary one course in each semester). After successful completion of these on-line courses the students shall provide their successful completion status/certificates to the CoE through their respective Departments.

            # 8. EVALUATION AND ASSESSMENT

            The performance of a student in a semester shall be evaluated through continuous class assessment, MSE and ESE. Both the MSE and ESE shall be University examinations and will be conducted as notified by the CoE of the University. The marks for continuous assessment (Sessional marks) shall be awarded at the end of the semester. The continuous assessment shall be based on class tests, assignments/tutorials, quizzes/viva-voce and attendance etc. The MSE/ESE shall comprise of written papers, practicals and viva-voce, inspection of certified course work in classes and laboratories, project work, design reports or by means of any combination of these methods.

            # Table-1: Evaluation Scheme

            |S. No.|Type of Course|Continuous Assessment (CA)|Mid-Semester Examination (MSE)|End-Semester Examination (ESE)|Continuous Assessment (CA)|End-Semester Examination (ES)|
            |---|---|---|---|---|---|---|
            |1|FE courses|Continuous Assessment only (100 marks)| | | | |
            ---
            |2|CC/FC/ED/EG/EO|25|25|50|Nil|Nil|
            |---|---|---|---|---|---|---|
            |3|CC/FC/ED/EG/EO|15|15|40|15|15|
            |4|Project I and Project II|Nil|Nil|Nil|40|60|
            |5|Training|Nil|Nil|Nil|40|60|
            |6|Audit Courses*|-|-|-|-|-|

            *The distribution of marks of practical and/or theory components for Audit courses shall be determined by the respective Departments.

            Table 2: Continuous Assessment

            |S. No.|Type of Course|Continuous Assessment (CA)|
            |---|---|---|
            |1|CC/FC/ED/EG/EO Theory with Tutorial|Two class tests, Assignments, Teachers’ assessment (quizzes, viva-voce, attendance)|
            | |CC/FC/ED/EG/EO Theory with Practical|One class test, One Lab test, Assignments/Projects, Teachers’ assessment|
            |2|FE courses|Two class tests, Assignments, Teachers’ assessment|
            |3|Project I /II|Mid-Semester Presentation, Report, Supervisor’s Assessment|
            |4|Training|As specified by the Department|
            |5|Audit Courses|As specified by the Department|

            # 9. GRADING

            The relative grading system shall be implemented in awarding the grades and SGPA/CGPA under CBCS. A 10-point grading system and corresponding grade points shall be used with the letter grades as given in Table 3.
            ---
            # Table 3: The Grades and the Grade Points

            |S. No.|Letter Grade|Letter Grade|Grade point| |
            |---|---|---|---|---|
            |1|O|Outstanding|10| |
            |2|A+|Excellent|9| |
            |3|A|Very Good|8| |
            |4|B+|Good|7| |
            |5|B|Above average|6| |
            |6|C|Average|5| |
            |7|D|Pass|4| |
            |8|F|Fail|0| |
            |9|421|"t|FD| |
            | |Fail due to detention| |0| |
            |10|Ab|9|Absent|0|
            |11|W|Withdrawal|NIL| |

            The award of the grades shall be based on the marks out of 100, as per the distribution of the various components given in Table 1.

            For the class strength of more than 30, a relative grading system shall be implemented and the grades shall be allotted on the basis of normalized score as described below and Table 4.

            # Table 4: Grade Allocation based on the Normalized Score

            |S. No.|Lower Range of NS|Grade|Upper Range of NS|
            |---|---|---|---|
            |1|&gt;1.5|O|--|
            |2|&gt;1.0|A+|≤ 1.5|
            |3|&gt;0.5|A|≤ 1.0|
            |4|&gt;0.0|B+|≤ 0.5|
            ---
            # 9. Grading System

            # 9.3

            The normalized score shall be rounded off to two decimal places.

            # 9.4

            Grade Moderation shall be undertaken for the adjustment of the grade boundaries as indicated in Table 4. These grade boundaries may be adjusted as follows:

            - a. No student can be awarded ‘D’ or better grade without securing at least 30% aggregate marks in a course.
            - b. No student can be awarded ‘O’ grade without securing at least 85% aggregate marks in a course.
            - c. No student can be awarded less than ‘D’ if he/she scores more than 40% aggregate marks in a course.
            - d. No student can be awarded less than ‘O’ if he/she scores more than 95% aggregate marks in a course.
            - e. In case of any difficulty, the absolute grading method suggested in Table 5 shall be used.
            - f. The final grade boundaries shall be retained in records.

            # 9.5

            For the class strength of less than or equal to 30, the grades shall be allotted on the basis of absolute grading as given in Table 5.

            |S. No.|Marks|Grade|Marks|
            |---|---|---|---|
            |1|≥ 90|O|< 100|
            |2|≥ 81|A+|< 90|
            |3|≥ 72|A|< 81|
            |4|≥ 63|B+|< 72|
            |5|≥ 54|B|< 63|
            ---
            # 9.6 Interpretation of the Grades

            |6|≥ 45|C|< 54|
            |---|---|---|---|
            |7|≥ 35|D|< 45|
            |8| |F|< 35|

            a. Fail grade: A student obtaining Grade F/FD/Ab shall be considered as failed and shall be required to register for the course again. In case of the elective courses, if the student does not want to register again in an elective course in which he/she has failed (for EG, ED, EO, FE courses but not for CC or FC courses), then he/she can register afresh for a new elective course. However, grades F/FD, as applicable, shall be mentioned in the Grade Card even after passing the course.

            b. ‘FD’ grade: The FD grade indicates fail due to shortage of attendance in a course.

            c. ‘W’ grade: This refers to the withdrawal from the courses other than core courses. Withdrawal shall be allowed as per the guidelines issued from time to time by the Dean Academics.

            d. Audit/FE courses: For audit courses, grades shall be indicated however this will not be counted for the computation of the SGPA/CGPA.

            # 9.7 Computation of the SGPA and CGPA

            a. The SGPA is the ratio of the sum of the product of the number of credits and the grade points scored in all the courses taken in a semester (including back-log courses), to the sum of the number of credits of all the courses taken by a student, that is:

            𝑆𝐺𝑃𝐴(𝑆𝑗) = ∑(𝐶𝑖 × 𝐺𝑖) / ∑ 𝐶𝑖

            where, 𝑆𝑗 is the 𝑗𝑡ℎ semester, 𝐶𝑖 is the number of credits of the course of that semester and 𝐺𝑖 is the grade point scored by the student in the course.

            b. The CGPA is also calculated in the same manner taking into account the best.
            ---
            162 credit courses of the student taken over all the semesters of a programme, that is:

            𝐶𝐺𝑃𝐴 = ∑(𝐶𝑖 × 𝐺𝑖)
            ∑ 𝐶

            where, 𝐶𝑖 is the number of credits of the course and is the grade point scored by the student in the course.

            c. The SGPA and CGPA shall be rounded off to 2 decimal points.

            d. CGPA shall be converted into percentage of marks by multiplying it with 10. Both CGPA and percentage shall be mentioned on the final transcript.

            # 10. EXAMINATIONS

            10.1. The Examination committee shall formulate the guidelines for maintaining the standards of examination.

            # 10.2. Question paper format for MSE and ESE:

            a. NSUT There shall be no choice in the question papers of the MSE.

            b. In the question papers of the ESE, there shall be questions from each unit in proportion to the contents of the specific units. However, there may be maximum 35% choices within the questions of each of the units.

            c. All course outcomes shall be addressed in MSE and/or ESE.

            # 10.3. Answer sheet evaluation:

            For courses with more than one section/examiner, the evaluation of ESE answer sheets may be carried out by checking one question by one group of examiners and similarly, other questions checked by other groups extending the procedure to whole lot of answer sheets during Centralized checking.

            # 10.4. External examiners may be appointed for ESE of practical/project and training based courses.

            # 11. ATTENDANCE AND DETENTION

            11.1. Students of the programme are expected to attend every lecture, tutorial and
            ---
            practical class scheduled for them.

            # 11. Attendance Requirements

            11.2. The students must have a minimum attendance of 75% of the total number of classes including lectures, tutorials and practicals, held in a subject till MSE/ESE in order to be eligible to appear in the MSE/ESE for that subject.

            11.3. The Dean Academics, may allow relaxation in the minimum requirement of attendance upto 10% for reasons to be recorded. This relaxation may be granted on the production of documents showing that the student was either busy in any authorized activities or was absent due to medical/other genuine reasons. The student should submit these documents to the HoD, within seven days of resuming the studies. Certificates submitted later will not be considered.

            11.4. Under exceptional circumstances, the Dean Academics may further relax the minimum attendance up to 5% on recommendation of a committee comprising of Dean Student Welfare, Dean of Faculty and HoD of the respective department.

            11.5. Relaxation in attendance may be granted for a maximum of 2 times during the duration of the programme.

            11.6. A student shall not be permitted to appear in the MSE/ESE if his/her attendance till MSE/ESE is below 60 % after relaxation given in clauses 11.3 and 11.4.

            11.7. Students who are not allowed to appear in the ESE due to shortage of attendance shall be awarded ‘FD’ grade. Such students shall have to register again for that course in subsequent years/summer semester to pass the course.

            11.8. A student can register again for a different elective course in subsequent years/summer semester and pass the elective course.

            11.9. The attendance shall be counted from the date of start of academic session. For first year students, attendance shall be counted from the date of the start of academic session or the actual date of admission, whichever is later.

            # 12. PROMOTION AND PASSING A COURSE

            12.1. There shall not be any restriction on promotion from an odd semester to the next even semester.
            ---
            # 12. Promotion and Registration Policies

            12.2. For promotion from even semester to the next odd semester (i.e. of the next academic year) the student has to fully clear either of the semester of the academic year or earn credits greater than or equal to minimum credit of either of the semester of the academic year.

            12.3. There shall be no supplementary examinations. A student who has failed in a course shall have to register again for the course in a subsequent year/summer semester.

            12.4. If the student does not want to register again in an elective course (that is, EG, ED, EO, FE but not CC or FC courses) then he/she can register again for a new elective course.

            12.5. Summer semester may be run for back log courses in which there are 10 or more registrations. Separate grade card shall be issued for the summer semester (if applicable).

            12.6. If a student wants to improve his/her grade in a course, he/she has to register again for the course. However, the student may register for a different elective course as per clause 12.4. Registration for improvement of grade in a course shall be allowed only once. However, the best grade in that particular course, shall be considered for computation of SGPA/CGPA.

            12.7. To pass a course, the student should score at least 30% marks separately in the ESE of theory and practical (wherever applicable) components of the course.

            # 13. Semester Withdrawal on Medical/Other Grounds

            A student may apply for withdrawal from the semester, if he/she so desires. However, in any case, the maximum span of the programme shall remain 7 years.

            # 14. Course Co-ordination Committee

            The Course Co-ordination Committee (CCC) shall comprise of all the teachers teaching a course. However, where less than three teachers are teaching the course, the HoD may nominate a three-member committee. The chairperson of the CCC shall be.
            ---
            # 14. Course Coordination Committee

            Nominated by the HoD, before the beginning of the semester. The Course Coordination Committee for project/training based courses shall comprise of five faculty members nominated and chaired by the HoD.

            # 14.1. The CCC shall have the following functions-

            - a. To lay the guidelines for teaching and evaluating the courses including the design of practicals, well in advance of the starting of the semester.
            - b. To coordinate the preparation of quizzes, assignments, test papers etc. for continuous assessment as described in Table 2. Projects and training based courses shall be dealt similarly.
            - c. Chairperson CCC shall set the MSE question paper.
            - d. Question Paper setters may be appointed from amongst the members of the CCC.
            - e. Examiners shall be appointed from amongst the members of the CCC.
            - f. A question paper moderation committee may be formed out of the members of CCC chaired by the Chairperson, CCC.
            - g. To consider the individual representation of the students about evaluation and take remedial action, if needed.

            # 15. Result, Award of Degree and Medals

            The results of all the University Examinations shall be declared by the CoE taking into consideration the following:

            # 15.1.

            Each B.Tech. programme consists of 170 credits. A student shall be eligible for the award of the B.Tech. degree if he/she has earned 162 or more credits, securing a minimum CGPA of 5.00.

            # 15.2.

            CGPA will be calculated at the end of the programme, on the basis of the best 162 credits earned by the student.

            # 15.3.

            The B. Tech. degree shall be awarded only after the eighth or final semester examination, based on the aggregate performance of the student.
            ---
            # 15. Award of Degree

            15.4. A student who qualifies for the award of the degree securing ‘D’ or above grades in the subjects amounting to 182 credits in his/her first attempt in eight consecutive semesters and secures a CGPA of 8.50, considering all 182 credits, as per stipulations of regulation number 7.9, shall be awarded FIRST DIVISION WITH HONOURS. The CGPA of such students shall also be computed on the basis of best 162 credits, excluding credits earned from on-line courses.

            15.5. A student who qualifies for the award of the degree securing ‘D’ or above grades in all the subjects in his/her first attempt in eight consecutive semesters and secures a CGPA of 8.00 or above shall be awarded FIRST DIVISION WITH DISTINCTION.

            15.6. A student who qualifies for the award of the degree by securing ‘D’ or above grades in all the subjects in the stipulated maximum duration for the B.Tech. programme and secures a CGPA not less than 6.50 shall be awarded FIRST DIVISION.

            15.7. All other students who qualify for the award of degree by securing ‘D’ or above grades in all the subjects in the stipulated maximum duration for the B.Tech. programme and secures a CGPA less than 6.50 shall be awarded SECOND DIVISION.

            15.8. The Gold, Silver and any other Medals as decided by the University shall be awarded to students, for each branch, from amongst those students who have been awarded first division with Honours/ Distinction.

            15.9. Students who have developed/demonstrated exceptionally innovative ideas/projects/designs etc. would be eligible to be considered for appropriate awards as per University norms.

            # 16. Scrutiny of Evaluation

            16.1. The answer sheets of MSE shall be displayed by the respective teacher in the class.

            16.2. The ESE awards shall be displayed after compilation of the marks, by the Chairperson CCC, on a declared date.

            16.3. Students willing to scrutinize his/her ESE answer sheets shall be allowed to do so by the course coordinator or his/her nominee on a declared date and venue.
            ---
            # 16. Retotalling and Rechecking

            16.4. Retotalling and rechecking of only the unchecked answers, if any, shall be permitted after the scrutiny of the answer sheets by the students.

            16.5. Students may submit a representation to the Chairperson CCC, in case of any grievance related to the evaluation.

            16.6. Grades shall be awarded as per the grade boundaries obtained for the course after considering the change in marks, if any.

            # 17. UNFAIR MEANS

            Cases of unfair means in any examination shall be dealt as per such Regulations as may be proposed by the Examination Committee and approved by the Senate and the BoM.

            # 18. CURRICULUM REVISION

            The curriculum shall be updated continuously as and when considered necessary, to keep pace with the advancements in the subject areas of the concerned B. Tech. programme.

            # 19. MIGRATION FROM NSIT (University of Delhi) DURING TRANSITION PERIOD

            Migration from NSIT, University of Delhi, to NSUT shall be allowed for the students having year-back and his/her credits shall be transferred as per the University norms. Migration shall not be permitted from any other university.

            # 20. STUDENT EXCHANGE PROGRAMME

            Transfer of credits from the organizations, with which the University has an MOU, to NSUT+, shall be allowed as per the University rules.

            # 21. INTERPRETATION OF THE REGULATIONS AND POWER TO MODIFY

            Subject to the provisions of the Act, the Statutes and the Regulations, the issues not covered in Regulations as above, or in the event of differences of the opinion/interpretation, the Vice-Chancellor may take a decision, after obtaining the
            ---
            opinion of the Advisory Committee. The decision of the Vice-Chancellor shall be final. However, this may not be taken as precedence for any similar cases in future.

            # The Advisory Committee shall consist of the following

            - a. Dean, Academics, Chairperson
            - b. Deans of the Faculties
            - c. Controller of Examinations
            - d. Two Chairpersons of BoS, as nominated by the Vice Chancellor
        """

        chat_context = f"""
            {{"context": {context}}}
            {{"role": "system", "content": "take it as context to answer the user query "{systemPrompt}}}
            {{"role": "user", "content": {message}, "history": {chatHistory}}}
        
        """

        response = await asyncio.to_thread(model.generate_content, chat_context)
        response_text = response.text

        references = [
            {"title": "Distributed Database", "url": "https://www.instagram.com/"},
            {"title": "Soft Computing", "url": "https://www.fallingfalling.com/"},
        ]

        return {"response": response_text, "references": references}

    except Exception as e:
        raise Exception(f"Error generating AI response: {str(e)}")
