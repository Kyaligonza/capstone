

# database_path = os.environ.get('DATABASE_URL')
# if not database_path:
#     database_name = "mycapstone"
#     database_path = "postgres://{}/{}".format('localhost:5432', database_name)

export DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/mycapstone'

# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/mycapstone'
export bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmNTg3ZWY5YjEwZjA0ZmQ5M2MzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDUzNjksImV4cCI6MTU4MTg1MjU2OSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.wxurZHZR-Y8o-8q8vfEgROiJjksN4LXfE0yWJZM-MpkJBQspwUqS6MUus_-qWC5Qn8BnHgfQNxx7WVpvax81Isloty1VwfwtgqKeua66oRc9999FYPftmT-CZmIkVB3bEqNB_fhFF8y3t4Vy2QoFmAvGV74TJVnCbsrQdxWmJENyL-ubABPPEJyKbUdKumB-dgIu7PIqVHp4Weclr6xYpB4buuhO4X4G37dS3Nzy1TSRmuRD4IotlE1FQBj7t3a9lfu5wNbReWsCHBd-Ptubw_ivdb4u4wC6jkgCoCT8tBQs9nS6XHlj-35tEwisnEMah4-RcswXAKi4CJ19MoE4tA",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjAxODA1LCJleHAiOjE1OTk2MDkwMDUsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.R_hDBzH-ci-IsVu7Mx277G29HBf9UnqQg2TaTkpQRmNdVp1giLknDX0qflPuiHwSWAJnKQeUsIFqOmLYO3SZsqtRfDdzq-QqNx3TISiS4CBSaeZ55doJnh2ql78ywNlx2f_hhgKNA5IWigSukbTvz_Zp0OcWh-Bi1BmY9LkGRyz25zpofPfq6LCBR_C61N50tY63qhvcOHq_v6NCFe7I21Cxy6Xw03GsI98WMot5nEixQ67tNb-QBn5ZCNBxe9rDQJ5rlp-Sbia0Ny__38EGxHA6UT5Q7P2h06zisaWY8ShX3brLu5EZRqiGTTMcjM6huN-hgn2lILyDbDN0Xz9q_w",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmOTA3ZWY5YjEwZjA0ZmQ5M2ZiIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDQ4NDUsImV4cCI6MTU4MTg1MjA0NSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZWRpdDphY3RvcnMiLCJlZGl0Om1vdmllcyIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.O9OO51LPinbfF8hc3HKKMmC8X9vrM4evMvS7iVXMSu5FqcHoe_J1t3aafNAIyYDKIJAExN_qINbKFcPw3DfDuW8-Bh5w8ffD-ODhYICAKaQngf1mDHzBy3bpCZ9IFetZF1lMV1OBRlR27SvvoEN-uH-8Cnea3gcWoah2aoxIqew18GKBBUlTKCm4qKJf3i7c9-LuEZrPHTBIx-mvllpIcvFPNyhSN3Xzj2tTRmcKuBgsvPdmqBnGYlaGsxpjXlFl9fuu31LICUKoSoOpUo-hY8DbBk0nwAKmS5TOTynfAnE6uUy1xDhDvGbD6s5qMUsYOTyKJvOmxIt9w5HDJDdZWA"
}