import os

# Gets the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    'AUTH0_DOMAIN': 'agent88.us.auth0.com',
    'ALGORITHMS': ['RS256'],
    'API_AUDIENCE': 'stars',
    'CLIENT_ID': 'xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ',
    'CLIENT_SECRET': ('euZkCMgG5Kq2gBRiB4zgiIi8p1-'
                      'eNOZ2RhIuBOuynF2mLVQdjpWOHC7DnS74ZR5_')
}

bearer_tokens = {
    "casting_assistant": ("Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6Ikp"
                          "XVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9."
                          "eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY"
                          "29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZWQ2OWM1MTA2MDA2"
                          "ZGUyMzNjNCIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwODExO"
                          "DgwLCJleHAiOjE2MDA4OTgyODAsImF6cCI6InhGb0c4Ujcx"
                          "RUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiI"
                          "iLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om"
                          "1vdmllcyJdfQ.UNc_I9utPjpp-kOMANBFNTQOI92yWY-GOP"
                          "kNt4lSXVMm8VdUmSXm5_24dlUpapJGKUA2glLSTWpk5qBi"
                          "4ip1ZDn7Dq_2RCluzZPx7zqzL5kgse2VIUuN7z5qPx5b"
                          "k_ZpuVLbVsmW1VsrZ2SUdClep7pqMtMjlfuQpC2gaz6"
                          "B4rJSwOKUit6sYnkvM11osOARGpit9NxeMGaCDfw"
                          "Fld_uf8JOiddfSW-rDXQSHYSNa4l4qc33D4HdCqK"
                          "50hKrrv5e8YP8pLDFeS6n5jDgu68311JxuQh7us"
                          "3l_sN4sDpv5OZwvoDdaGAD5VvN91KfeMS6gQv0"
                          "41IeDAMFdd6LKpvFUg"),
    "executive_producer": ("Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC"
                           "IsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9."
                           "eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY"
                           "29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA"
                           "2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAw"
                           "ODExMzYyLCJleHAiOjE2MDA4OTc3NjIsImF6cCI6InhGb0c"
                           "4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUi"
                           "OiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwi"
                           "ZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW"
                           "92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW"
                           "92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdm"
                           "llcyJdfQ.ivUg3eiI4SBFsLmhrnkWnivxKBu9QhNitG"
                           "3FW2xUHJeoD6gbAszFSlRX_r1_-LXuUV3j1UZIKC"
                           "OMokjjEvxxfzIgMIN6-92y4RJmJkvHjOoVgLvGTc"
                           "7IJDcEzdmvNTFVZbPjwtaOzoLNdM8uxw_rSd2vhj"
                           "4luaPAnLaLEnf4x83i8VLAASKqi9a5d2ri4t0rDc0y7q"
                           "6vT9so2zB91qPRN1mdxOUahUo8fC9CyTqBJOG58CKzfbH"
                           "5_3yQV4IBBhVV3qTM4yVFLMiICKtrDLRlpKEHqUrTd2-h-rs"
                           "5NWQf6sjtXjRxekJELY5E9JGHT86sJ5i84QbQ8EVAS"
                           "39damncWg"),
    "casting_director": ("Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZC"
                         "I6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9."
                         "eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY"
                         "29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZGMxMjA3NmE3MDA"
                         "2NzhmODM4OSIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAw"
                         "ODExNTk5LCJleHAiOjE2MDA4OTc5OTksImF6cCI6InhGb0c"
                         "4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic"
                         "2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b"
                         "3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXR"
                         "jaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG"
                         "9ycyJdfQ.NBC446VZgBDlqpnjphEQmKv3Ku6HZHWtpPowbTcqNR"
                         "7GLEWmi1C6TT-IcsUvmu5qabMMAK5FGic_tzCy"
                         "8OarnWoKBjJufuWXdlr02bFDr4g8XLGTq0BfB16Ckg8d6ab9z"
                         "65icXyel4va3ZxRHIB0eInbdLhO7xkwNh9SJTb3beeyHun"
                         "IRWVF2GZJEFrc4dsmflfUlRQF3OZWNit5jb2dVouJTqb"
                         "lkRetIidz4C8Px_uVovvauT0w6g0Y9LXqLe86__O_oJYZ"
                         "3Ti7ZELhDoG3yT9rMVjUKn3K_ELdO6t2y2WtQAom"
                         "5zK8_0vn8kPLYoNf0XewoFhYBwf1dE-s5vNSwQ")
}
