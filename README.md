# ctsi-2020-hackathon-omop
Code created as part of the two hour St. Patrick's day hackathon around the OMOP data model and the spread of infectious disease

1. edit your .env file
1. pipenv install
1. python scratch.py

***all patients with influenza (cohort 1) 

select subject_id as person_id from cohort where cohort_definition_id = '1'; 