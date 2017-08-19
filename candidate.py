import pandas as pd

#Files
candidates='Candidates.xlsx'
jobs='Jobs.xlsx'

#Read Files
dfJobs=pd.read_excel(jobs)
dfCandidates=pd.ExcelFile(candidates)

#Target Skills For 14 Jobs
#Remove End commas and change all skills to small case and unique ones
total_job_skills=[]
for i, skill in enumerate(dfJobs['SKILLS']):
    total_job_skills.append(list(set([x.strip() for x in skill.rstrip(',').lower().split(',')])))

candidate_skills=[]
candidate_sheets=dfCandidates.sheet_names

all_candidates_for_all_job=[]
all_candidate_experiences_all_job=[]
for sheet in candidate_sheets:
    all_candidate_experiences_single_job=[]
    all_candidates_for_single_job=[]
    for i, skill in enumerate(dfCandidates.parse(sheet)['CVSkills']):
        all_candidates_for_single_job.append(list(set([x.strip() for x in skill.rstrip(',').lower().split(',')])))
        all_candidate_experiences_single_job.append(dfCandidates.parse(sheet)['Experience'][i])
    all_candidates_for_all_job.append(all_candidates_for_single_job)
    all_candidate_experiences_all_job.append(all_candidate_experiences_single_job)

print("Total Jobs:  ",len(total_job_skills))
print("Total Jobs: ", len(all_candidates_for_all_job))
if len(total_job_skills)==len(all_candidates_for_all_job):
    print("All Good!")
else:
    print("Something not good")

##Total Jobs
total_jobs=len(all_candidates_for_all_job)

#all_candidate_for_all_job ==> single_job ==> Single CV ===> Single skill
count_matched_skills_for_total_job=[]
matched_skills_for_total_job=[]
for i,single_job_candidates in enumerate(all_candidates_for_all_job):
    # count_matched_skills_for_single_job=[]
    matched_skills_for_single_job=[]
    for j, single_cv in enumerate(single_job_candidates):
        # count_matched_skills_for_single_cv=[]
        matched_skills_for_single_cv=[]
        for single_skill in single_cv:
            if single_skill in total_job_skills[i]:
                matched_skills_for_single_cv.append(single_skill)
        
        matched_skills_for_single_job.append(matched_skills_for_single_cv)
        # count_matched_skills_for_single_cv.append(len(matched_skills_for_single_cv))
    matched_skills_for_total_job.append(matched_skills_for_single_job)
    # count_matched_skills_for_single_job.append(len(matched_skills_for_single_job))


if len(total_job_skills)==len(matched_skills_for_total_job):
    print("-----------Again-----All Good!")
#for First Job:
matched_skills_total_job_count=[]
for i,matched_cvs_single_job in enumerate(matched_skills_for_total_job):
    matched_skills_single_job_count=[]
    for matched_single_cv in matched_cvs_single_job:
        matched_skills_single_job_count.append(len(matched_single_cv))
    matched_skills_total_job_count.append(matched_skills_single_job_count)

print('Job Skills Score for Fist Job: \n')
print([x for x in matched_skills_total_job_count[0]])

print('Experiences for First Job: \n')
print(all_candidate_experiences_all_job[0])

list_skills_score=[]
list_experiences_score=[]
total_candidate_Score=[]
list_experience_filtered=[]
list_skills_filtered=[]
total_score_filtered=[]
for i in range(len(matched_skills_total_job_count)):
    single_list_skills=[100*x/max(matched_skills_total_job_count[i]) for x in matched_skills_total_job_count[i]]
    list_skills_score.append(single_list_skills)


    single_list_experience=[100*x/max(all_candidate_experiences_all_job[i]) for x in all_candidate_experiences_all_job[i]]
    list_experiences_score.append(single_list_experience)
    #Most Experienced 
    # temp=[0.7*x if x>=70 else x for x in single_list_experience]
    # temp=[0.5*x if x>=50 and x<70 else x for x in temp]
    # temp=[0.3*x if x<50 else x for x in temp]
    temp=[0.5*x for x in single_list_experience]
    list_experience_filtered.append(temp)

    #Most Skilled
    # temp_skills=[0.7*x if x>=70 else x for x in single_list_skills]
    # temp_skills=[0.5*x if x>=70 else x for x in temp_skills]
    # temp_skills=[0.3*x if x>=70 else x for x in temp_skills]
    temp_skills=[0.5*x for x in single_list_skills]
    list_skills_filtered.append(temp_skills)

    #Total Score
    total_score_filtered.append([a+b for a, b in zip(temp, temp_skills)])



print('Experence Score in %: \n')
print(list_experiences_score[0])

print(' \n Expereint Score with Filtered>70\n ')
print(list_experience_filtered[0])

print('Skills Score in %: \n')
print(list_skills_score[0])

print('\nSkills Score Filtered in %: \n')
print(list_skills_filtered[0])

print('\nTotal Scores: \n ')
print(total_score_filtered[0])


df_totalScore0=pd.DataFrame(total_score_filtered)
df_totalScore0.T.to_csv("file1.csv", sep=',',index=False)



# matched_skills_total=[]
# for i,cv in enumerate(processed_skill):
#     matched_skills=[]
#     for skill in cv:
#         if skill in total_job_skills[i]:
#             matched_skills.append(skill)
#     matched_skills_total.append(matched_skills)
