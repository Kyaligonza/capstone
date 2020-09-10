

# database_path = os.environ.get('DATABASE_URL')
# if not database_path:
#     database_name = "mycapstone"
#     database_path = "postgres://{}/{}".format('localhost:5432', database_name)

export DATABASE_URL='postgresql://postgres:postgres@localhost:5432/mycapstone'

# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/mycapstone'
# export bearer_tokens = {
#     "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmNTg3ZWY5YjEwZjA0ZmQ5M2MzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDUzNjksImV4cCI6MTU4MTg1MjU2OSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.wxurZHZR-Y8o-8q8vfEgROiJjksN4LXfE0yWJZM-MpkJBQspwUqS6MUus_-qWC5Qn8BnHgfQNxx7WVpvax81Isloty1VwfwtgqKeua66oRc9999FYPftmT-CZmIkVB3bEqNB_fhFF8y3t4Vy2QoFmAvGV74TJVnCbsrQdxWmJENyL-ubABPPEJyKbUdKumB-dgIu7PIqVHp4Weclr6xYpB4buuhO4X4G37dS3Nzy1TSRmuRD4IotlE1FQBj7t3a9lfu5wNbReWsCHBd-Ptubw_ivdb4u4wC6jkgCoCT8tBQs9nS6XHlj-35tEwisnEMah4-RcswXAKi4CJ19MoE4tA",
#     "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjAzNDExLCJleHAiOjE1OTk2MTA2MTEsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.iYVfVvA3rnkVJttJYzrUVQFyQcXpYsq_JXOv_kPN3cAwaC2ziXs4BUr6iTFobtQQ-Nbc8LEO9GiLy1vyODGciVhttZfJCWRUZpp_MuHZv1_MEO54NM09hwWFNToeYPAB-FM_VR6muJ_VtBIdcUi49m6WhvM7SLpCwTjwuvKuDWCeB5m2TrGT7byt6UDafFH59jDh6KAVWSVHKsCE7SNzC3kTqs5SZ-mziqsq7qvuLSdIQz0xieEq6ieXksxP57EYRBIxJNLCrjDdVrgY_1s7lQTd4RHDhGugKrgHWevZ0bRHGCAj-l8rM1cq7gqDk9C04NFJcmkwr6KFFE_cIFIVDA",
#     "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmOTA3ZWY5YjEwZjA0ZmQ5M2ZiIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDQ4NDUsImV4cCI6MTU4MTg1MjA0NSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZWRpdDphY3RvcnMiLCJlZGl0Om1vdmllcyIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.O9OO51LPinbfF8hc3HKKMmC8X9vrM4evMvS7iVXMSu5FqcHoe_J1t3aafNAIyYDKIJAExN_qINbKFcPw3DfDuW8-Bh5w8ffD-ODhYICAKaQngf1mDHzBy3bpCZ9IFetZF1lMV1OBRlR27SvvoEN-uH-8Cnea3gcWoah2aoxIqew18GKBBUlTKCm4qKJf3i7c9-LuEZrPHTBIx-mvllpIcvFPNyhSN3Xzj2tTRmcKuBgsvPdmqBnGYlaGsxpjXlFl9fuu31LICUKoSoOpUo-hY8DbBk0nwAKmS5TOTynfAnE6uUy1xDhDvGbD6s5qMUsYOTyKJvOmxIt9w5HDJDdZWA"
# }
export DATABASE_URL=postgres://mlckhnhmfeebkn:56609773021eab28355d7422cc60d76fe1621783b728229d0eb5a8ed813f69d5@ec2-3-215-207-12.compute-1.amazonaws.com:5432/dfdlvhhslmvnfe
export AUTH0_DOMAIN='agent88.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE=stars
export CLIENT_ID=xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ
export CLIENT_SECRET=euZkCMgG5Kq2gBRiB4zgiIi8p1-eNOZ2RhIuBOuynF2mLVQdjpWOHC7DnS74ZR5_
export FLASK_APP=app.py

export assistant_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1kQkVTMU1YVHFhejlzQ2Q4eGV0byJ9.eyJpc3MiOiJodHRwczovL2Rldi03MXR0MWo5Yi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwYzRjOWFhMWY2MDMwMDE5YjBiNmMwIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU5OTI1MjQ2NywiZXhwIjoxNTk5MzM4ODY3LCJhenAiOiJLT2V1cVcyWjZ0UHdVQXF1VnFsUWwxdkxNQ2F4VkhzeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.JG6mdwLTrnRz1jxy-ZgHfSp2RICD7FtGcDiRwdkkJpa84klf9SyCpNgv9F52BgaH9_VTWt47KD6mkNzGfOZtqNXJ-C3HqTmckKQfGbgcNBpyxGbrnp8WvYQqaCyuscqAJ2UrssNp0o1oyqwn2Yn1tu6oxIYQyvJofZhetsiiYgyTJLWyCEg03xjH7E2aJyZjK6dhvjQMAtE9rOUvWQaenutVEJQuTl9eD0fhlTgE9Dfd5lkQn_ghKy0v6bsNlyL4awwPmUie8KOiw-pAlWM2-2chEmVgOGnFjje6ZQ-MywUMMYJnPugCieaO575iGoYjBCL5NgAPtCrXf5ae1QKVAw'
export direct_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1kQkVTMU1YVHFhejlzQ2Q4eGV0byJ9.eyJpc3MiOiJodHRwczovL2Rldi03MXR0MWo5Yi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwYzRjYWNhMWY2MDMwMDE5YjBiNmMyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU5OTI1MjUwNCwiZXhwIjoxNTk5MzM4OTA0LCJhenAiOiJLT2V1cVcyWjZ0UHdVQXF1VnFsUWwxdkxNQ2F4VkhzeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDpuZXdfYWN0b3IiXX0.fv7KWAP9jYkCd03BwG6M43fMJyfI2WI0Ir9srDKr5X6QbpwNmE7aBu9Xb4Fw9PFTqI_a7kR-CnqvxVM2xNjEPwSvjgJbrhgcqjbVDvAR3mgaLbFPEtZROq21PAklkxUDGUgMh3tMA2GZNrzbmv4zIi_yi4oqmeLQ_TfUbCu49ZcWE4UrxNcnxr6e8P1cyh_T7VB3_9tZQqXitl7tSv61zIzSC2nSk3IVEcEfJrA020ZK5ECHTFaOScdmq_HG3FJh1XBlDLD26GCkBWstLtBbTAmGZ3wPS9V_1l7OAajBOqmYsFwA4xlGSMh9ZeMQb3eMEWSydES7wlEx3u1pUt7D9A'
export producer_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjEyMDkxLCJleHAiOjE1OTk2MTkyOTEsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Ej6CbOX7jmUZMqQustsgru1Am1_3VSq6uZrNO9gGlfloEi0GZ_ux7yeXFy5yoz7uqe-O9X_d8krdoq_RNdsh0jQpqqT4kG25zmxk0jKyAR4A-aFTMiZRH345-ned3HfmEaeIcXgdj0f4VdROf72mJg1JmlS_J-jb0cqEcKWH1OdveX3-2jdCTm6C23gTlDqzQBgGzd-ogMjJjnUtgSctFmVP93t1D6Q3uBzhnSV3aGEg5-h7Ma1VOhbROzcaB8OLmzA426gfE3L3lFvBD2EuNK1CX4z4tSOKmk3brN_-zVaFf4VOuDYnECc1Pj9o_YhJ--FJSbjbFTEhwpAKhLmVxQ'
# export EXCITED=true
