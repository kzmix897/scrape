import csv
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Masukkan API ID, API Hash, dan Nama Session
api_id = '29050819'
api_hash = 'e801321d49ec12a06f52a91ee3ff284e'
phone_number = '+6285945755344'  # Nomor telepon akun Telegram Anda

# Nama file CSV untuk menyimpan hasil scraping
output_file = 'group_members.csv'

# Fungsi untuk menyimpan data ke CSV
def save_to_csv(members):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Username', 'First Name', 'Last Name'])  # Header
        for member in members:
            writer.writerow([member.id, member.username, member.first_name, member.last_name])
    print(f"Data berhasil disimpan di {output_file}")

# Fungsi untuk scraping data anggota dari grup
async def scrape_members(client, group_username):
    # Mendapatkan entitas grup yang ditargetkan
    group = await client.get_entity(group_username)
    print(f"Mengambil anggota dari grup: {group.title}")

    # Mengambil semua anggota dari grup
    all_participants = await client.get_participants(group)
    members = []

    # Menyimpan data yang relevan
    for participant in all_participants:
        members.append(participant)
        print(f"Mengambil data: {participant.id}, {participant.username}")

    # Simpan hasil ke CSV
    save_to_csv(members)

# Fungsi utama untuk menjalankan skrip
async def main():
    # Membuat klien Telegram
    async with TelegramClient(phone_number, api_id, api_hash) as client:
        group_username = input("Masukkan username grup (misalnya @nama_grup): ")
        await scrape_members(client, group_username)

# Jalankan fungsi utama
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
