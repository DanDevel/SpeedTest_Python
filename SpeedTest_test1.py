import speedtest

def testar_velocidade_internet():
    st = speedtest.Speedtest()
    print("Testando a velocidade da internet...")
    download_speed = st.download() / 10**6  # convertendo para megabits por segundo
    upload_speed = st.upload() / 10**6  # convertendo para megabits por segundo
    print(f"Velocidade de Download: {download_speed:.2f} Mbps")
    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    testar_velocidade_internet()
