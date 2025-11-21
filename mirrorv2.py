from telethon.sync import TelegramClient, events
from telethon import utils 
import logging
import os
import asyncio



SIGNATURE_MARKDOWN = """

"""


def add_signature_markdown(text):
    return f"{text}\n\n{SIGNATURE_MARKDOWN}"



logging.basicConfig(format='[%(levelname)s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)


def gorev_emrini_oku(dosya_adi="ayarlar.txt"):
    logging.info(f"{dosya_adi} dosyasından görev emri okunuyor...")
    try:
        ayarlar = {}
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            for satir in f:
                satir = satir.strip()
                if not satir or satir.startswith('#'): continue
                if '=' in satir:
                    anahtar, deger = satir.split('=', 1)
                    ayarlar[anahtar.strip()] = deger.strip()
        gerekli_anahtarlar = ['API_ID', 'API_HASH', 'SESSION_NAME', 'KAYNAK_KANAL_ID', 'HEDEF_KANAL_ID']
        for anahtar in gerekli_anahtarlar:
            if anahtar not in ayarlar or not ayarlar[anahtar]:
                logging.critical(f"KRİTİK HATA: Görev emri dosyasında '{anahtar}' maddesi eksik veya boş!")
                sys.exit()
        logging.info("Görev emri başarıyla okundu ve doğrulandı.")
        return ayarlar
    except FileNotFoundError:
        logging.critical(f"KRİTİK HATA: '{dosya_adi}' görev emri dosyası bulunamadı!")
        sys.exit()
AYARLAR = gorev_emrini_oku()


API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_NAME = os.environ.get('SESSION_NAME')
KAYNAK_KANAL_ID = int(os.environ.get('KAYNAK_KANAL_ID'))
HEDEF_KANAL_ID = int(os.environ.get('HEDEF_KANAL_ID'))


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=KAYNAK_KANAL_ID))
async def handler(event):
    try:
        msg = event.message


        sent_message = await client.send_message(
            HEDEF_KANAL_ID,
            message=msg,
            link_preview=True
        )
        
       # await client.send_message(
      #      HEDEF_KANAL_ID,
      #      SIGNATURE_MARKDOWN,
      #      reply_to=sent_message.id,
       #     parse_mode="md",         
       #     link_preview=True
       # )

    except Exception as e:
        logging.error(f"HATA: {e}")

async def main():
    logging.info("Hayalet İletici (Son Kan) operasyonu başlatılıyor...")
    await client.start()
    logging.info("Bağlantı başarılı. Nöbetçi birlik devrede.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):

        logging.info("Operasyon manuel olarak sonlandırıldı.")

