##===STUDI KASUS 1===##

data_mahasiswa = [
 {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
 {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
 {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
 {"nama": "Azka", "nim": "230104", "tugas": 77, "uts": 84, "uas": 82},
 {"nama": "Rina", "nim": "230105", "tugas": 81, "uts": 89, "uas": 86},
]
mhs_berprestasi = [mhs for mhs in data_mahasiswa if (mhs['tugas']*0.3)+(mhs['uts']*0.3)+(mhs['uas']*0.4) > 80]

ranking_mhs = sorted(data_mahasiswa, key=lambda mhs: (mhs["tugas"]*0.3)+(mhs["uts"]*0.3)+(mhs["uas"]*0.4), reverse= True )

print(f"Mahasiswa terbaik adalah {ranking_mhs[0]['nama']} Dengan NIM {ranking_mhs[0]['nim']}")

