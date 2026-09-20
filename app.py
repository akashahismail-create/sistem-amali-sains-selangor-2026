import streamlit as st
import os
import pandas as pd
from datetime import datetime, date, timedelta
from pathlib import Path
import json

st.set_page_config(page_title="JPN Selangor - Amali Sains 2026", layout="wide", page_icon="🧪")

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False
if "menu_amali" not in st.session_state:
    st.session_state["menu_amali"] = "Dashboard"

# ===== FIX PATH UNTUK GITHUB / STREAMLIT CLOUD =====
BASE_DIR = Path(__file__).parent
FILE_EXCEL_CANDIDATES = [
    BASE_DIR / "data_pusat_amali_sains_baru.xlsx",
    BASE_DIR / "data_pusat_amali_sains_BETUL.xlsx",
    BASE_DIR / "data_pusat_amali_sains_baru (1).xlsx",
    Path("data_pusat_amali_sains_baru.xlsx"),
    Path("data_pusat_amali_sains_BETUL.xlsx"),
]

FILE_EXCEL = None
for p in FILE_EXCEL_CANDIDATES:
    if p.exists():
        FILE_EXCEL = p
        break

# Fallback kalau masih tak jumpa
if FILE_EXCEL is None:
    FILE_EXCEL = BASE_DIR / "data_pusat_amali_sains_baru.xlsx"

FILE_NOTIS = BASE_DIR / "pemberitahuan.json"
DEFAULT_NOTIS = "📢 MAKLUMAN TERKINI: DATA TELAH DIKEMASKINI IKUT LAPORAN RASMI LEMBAGA PEPERIKSAAN (CRViewer 60 & 61). 473 MAKMAL SAH, 287 PUSAT. KAPASITI 20 CALON PER SIDANG. SEBARANG PERTANYAAN SILA HUBUNGI SEKTOR PENTAKSIRAN DAN PEPERIKSAAN JPN SELANGOR"

# ===== CSS SPM STYLE - KIRI MENU HIJAU (KEKAL) =====
dark_bg = "#121212" if st.session_state["dark_mode"] else "#FAFAFA"

hide_style = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap');
#MainMenu {{visibility: hidden; height: 0px;}}
footer {{visibility: hidden; height: 0px;}}
header {{visibility: hidden; height: 0px;}}
div.block-container {{padding-top: 0.5rem!important; background: {dark_bg}!important;}}
.hero-banner {{
    background: linear-gradient(135deg, #004D40 0%, #00695C 25%, #00897B 50%, #00695C 75%, #004D40 100%);
    border: 3px solid #FFD700; border-radius: 20px; padding: 18px 24px; margin-bottom: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
}}
.hero-title {{color: #FFD700; font-size: 26px; font-weight: 800; font-family: 'Poppins'; letter-spacing: 1px;}}
.hero-subtitle {{color: white; font-size: 16px; font-weight: 600;}}
.hero-spm {{color: #FFD700; font-size: 13px; font-weight: bold; margin-top: 8px; border-top: 2px solid rgba(255,215,0,0.5); padding-top: 6px;}}
section.main > div.block-container > div[data-testid="stVerticalBlock"] > div > div[data-testid="stHorizontalBlock"]:nth-child(2) > div[data-testid="column"]:nth-child(1) > div[data-testid="stVerticalBlock"] {{
    background: linear-gradient(180deg, #00695C 0%, #004D40 100%)!important;
    border-radius: 16px!important; padding: 14px!important;
    border: 2px solid #FFD700!important; box-shadow: 0 4px 15px rgba(0,0,0,0.3)!important;
}}
div[data-testid="stColumn"]:nth-child(1) button {{
    background: linear-gradient(135deg, #00897B 0%, #00695C 100%)!important;
    color: #FFEB3B!important; border: 2px solid #FFD700!important;
    border-radius: 10px!important; font-weight: 700!important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2)!important; margin-bottom: 4px!important;
}}
div[data-testid="stColumn"]:nth-child(1) button:hover {{
    background: linear-gradient(135deg, #00ACC1 0%, #00838F 100%)!important;
    color: white!important; border-color: #FFEB3B!important;
    box-shadow: 0 0 15px rgba(255,215,0,0.7)!important; transform: translateY(-2px)!important;
}}
.kpi-card {{
    background: linear-gradient(135deg, #00695C 0%, #004D40 100%);
    border: 2.5px solid #FFD700; border-radius: 12px; padding: 12px; text-align: center;
    min-height: 80px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}}
.kpi-label {{color: #FFEB3B; font-size: 10px; font-weight: 700; text-transform: uppercase;}}
.kpi-value {{color: #FFD700; font-size: 26px; font-weight: 800;}}
@keyframes blinkGold {{0%{{box-shadow:0 0 10px rgba(255,215,0,0.5);}}50%{{box-shadow:0 0 20px rgba(255,215,0,1);}}100%{{box-shadow:0 0 10px rgba(255,215,0,0.5);}}}}
.countdown-box {{animation: blinkGold 1.5s infinite;}}
.marquee-container {{
    background: linear-gradient(90deg, #B71C1C 0%, #D32F2F 50%, #B71C1C 100%);
    border: 3px solid #FFD700; border-radius: 10px; padding: 10px 0; margin: 10px 0 15px 0;
    overflow: hidden; white-space: nowrap; box-shadow: 0 4px 15px rgba(183,28,28,0.6);
}}
.marquee-text {{
    display: inline-block; padding-left: 100%; animation: marquee 60s linear infinite;
    color: white; font-weight: 800; font-size: 14px;
}}
@keyframes marquee {{0% {{ transform: translate(0, 0); }} 100% {{ transform: translate(-100%, 0); }}}}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

try:
    from zoneinfo import ZoneInfo
    now_my = datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
except:
    now_my = datetime.utcnow() + timedelta(hours=8)
HARI_INI = now_my.date()
TARIKH_AMALI = date(2026, 11, 16)
delta = (TARIKH_AMALI - HARI_INI).days
countdown_num = str(max(delta, 0))

st.markdown(f"""
<div class="hero-banner">
    <div style="display:flex; align-items:center;">
        <div style="font-size:45px; margin-right:15px;">🧪</div>
        <div>
            <div class="hero-title">JABATAN PENDIDIKAN SELANGOR</div>
            <div class="hero-subtitle">SEKTOR PENTAKSIRAN DAN PEPERIKSAAN</div>
            <div class="hero-spm">🧪 SIJIL PELAJARAN MALAYSIA 2026 🧪 | SISTEM PENGURUSAN UJIAN AMALI SAINS SELANGOR</div>
            <div style="font-size:10px; color:#FFEB3B; margin-top:4px;">📅 Amali Sains: 16 November 2026 | Hari ini: {HARI_INI.strftime('%d %B %Y')} | {now_my.strftime('%I:%M %p')} MY | Data LP Rasmi | File: {FILE_EXCEL.name if FILE_EXCEL else 'TIADA'}</div>
        </div>
        <div style="margin-left:auto;">
            <div class="countdown-box" style="background: linear-gradient(135deg, #004D40, #00695C); border:3px solid gold; border-radius:12px; padding:8px 14px; text-align:center; min-width:120px;">
                <div style="color:#FFEB3B; font-size:9px; font-weight:800;">⏳ COUNTDOWN AMALI</div>
                <div style="color:white; font-size:32px; font-weight:900;">{countdown_num}</div>
                <div style="color:gold; font-size:8px; font-weight:700;">HARI LAGI - 16 NOV 2026</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

def baca_notis():
    try:
        if FILE_NOTIS.exists():
            with open(FILE_NOTIS, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "notis" in data:
                    return data["notis"]
        return DEFAULT_NOTIS
    except:
        return DEFAULT_NOTIS

def simpan_notis(teks):
    try:
        with open(FILE_NOTIS, "w", encoding="utf-8") as f:
            json.dump({"notis": teks, "tarikh": datetime.now().strftime("%d/%m/%Y %H:%M")}, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"Gagal simpan notis: {e}")
        return False

NOTIS_SEMASA = baca_notis()
st.markdown(f'<div class="marquee-container"><div class="marquee-text">{NOTIS_SEMASA} &nbsp;&nbsp; | &nbsp;&nbsp; {NOTIS_SEMASA}</div></div>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        if FILE_EXCEL and FILE_EXCEL.exists():
            xls = pd.ExcelFile(FILE_EXCEL)
            df_r = pd.read_excel(xls, sheet_name="Ringkasan_Makmal") if "Ringkasan_Makmal" in xls.sheet_names else pd.DataFrame()
            df_d = pd.read_excel(xls, sheet_name="Data_Pusat_Amali_Sains") if "Data_Pusat_Amali_Sains" in xls.sheet_names else pd.DataFrame()
            df_full = pd.read_excel(xls, sheet_name="Detail_Sidang_Penuh") if "Detail_Sidang_Penuh" in xls.sheet_names else pd.DataFrame()
            return df_r, df_d, df_full, str(FILE_EXCEL), None
        else:
            return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), str(FILE_EXCEL), f"File tidak wujud: {FILE_EXCEL}. Sila pastikan file xlsx ada dalam repo GitHub."
    except Exception as e:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), str(FILE_EXCEL), f"Error baca Excel: {e}"

df_ringkasan, df_detail, df_full, file_used, error_msg = load_data()

PPD_NAMA = {"BA":"KLANG","BB":"KUALA LANGAT","BC":"KUALA SELANGOR","BD":"HULU LANGAT","BE":"HULU SELANGOR","BF":"SABAK BERNAM","BG":"GOMBAK","BH":"PETALING PERDANA","BJ":"SEPANG","BK":"PETALING UTAMA"}

col_menu, col_content = st.columns([1, 4])

with col_menu:
    st.markdown("<div style='color:#FFD700; font-weight:800; font-size:14px; text-align:center; margin-bottom:10px;'>🧭 MENU AMALI</div>", unsafe_allow_html=True)
    for m in ["Dashboard","Ringkasan Pusat","Senarai Makmal Full","Senarai Sidang","Analisis","Cari Sekolah","Selenggara Data"]:
        if st.button(m, key=f"menu_{m}", use_container_width=True):
            st.session_state["menu_amali"] = m
            st.rerun()
    st.markdown("---")
    if error_msg:
        st.error(error_msg)
    st.markdown(f"<div style='background:#004D40; border:1px solid gold; border-radius:8px; padding:8px; font-size:10px; color:#FFEB3B; text-align:center;'>📂 File: {Path(file_used).name}<br>📊 {len(df_ringkasan)} Makmal<br>🏫 {df_ringkasan['No_Pusat'].nunique() if not df_ringkasan.empty else 0} Pusat</div>", unsafe_allow_html=True)

menu = st.session_state["menu_amali"]

with col_content:
    if error_msg:
        st.warning(f"⚠️ {error_msg}")
        st.info("Pastikan dalam GitHub repo ada file: data_pusat_amali_sains_baru.xlsx (473 makmal) di root folder sama dengan app.py")

    if menu == "Dashboard":
        st.subheader("📊 Dashboard Amali Sains 2026 - Data Rasmi LP")
        if not df_ringkasan.empty:
            total_makmal = len(df_ringkasan)
            total_pusat = df_ringkasan["No_Pusat"].nunique()
            total_calon = df_ringkasan["Jumlah_Calon"].sum()
            total_sidang = df_ringkasan["Fizik_Sidang"].sum() + df_ringkasan["Kimia_Sidang"].sum() + df_ringkasan["Biologi_Sidang"].sum() + df_ringkasan["Sains_Tambahan_Sidang"].sum()
            k1,k2,k3,k4 = st.columns(4)
            with k1: st.markdown(f"<div class='kpi-card'><div class='kpi-label'>Jumlah Makmal</div><div class='kpi-value'>{total_makmal}</div></div>", unsafe_allow_html=True)
            with k2: st.markdown(f"<div class='kpi-card'><div class='kpi-label'>Jumlah Pusat</div><div class='kpi-value'>{total_pusat}</div></div>", unsafe_allow_html=True)
            with k3: st.markdown(f"<div class='kpi-card'><div class='kpi-label'>Jumlah Calon</div><div class='kpi-value'>{total_calon}</div></div>", unsafe_allow_html=True)
            with k4: st.markdown(f"<div class='kpi-card'><div class='kpi-label'>Jumlah Sidang</div><div class='kpi-value'>{total_sidang}</div></div>", unsafe_allow_html=True)
            st.write("")
            c1,c2,c3,c4 = st.columns(4)
            with c1: st.metric("Fizik", int(df_ringkasan["Fizik_Sidang"].sum()))
            with c2: st.metric("Kimia", int(df_ringkasan["Kimia_Sidang"].sum()))
            with c3: st.metric("Biologi", int(df_ringkasan["Biologi_Sidang"].sum()))
            with c4: st.metric("Sains Tambahan", int(df_ringkasan["Sains_Tambahan_Sidang"].sum()))
            st.markdown("---")
            st.markdown("### 🗺️ Pecahan Ikut PPD")
            if "Kod_PPD" in df_ringkasan.columns:
                ppd_count = df_ringkasan.groupby("Kod_PPD").agg(Bil_Makmal=("Nama_Makmal","count"), Bil_Pusat=("No_Pusat","nunique"), Fizik=("Fizik_Sidang","sum"), Kimia=("Kimia_Sidang","sum"), Biologi=("Biologi_Sidang","sum"), ST=("Sains_Tambahan_Sidang","sum")).reset_index()
                ppd_count["Daerah"] = ppd_count["Kod_PPD"].map(PPD_NAMA)
                st.dataframe(ppd_count, use_container_width=True, hide_index=True)
            s_tambahan_pusat = df_ringkasan.groupby(["No_Pusat","Nama_Sekolah"])["Sains_Tambahan_Sidang"].sum().reset_index()
            lebih = s_tambahan_pusat[s_tambahan_pusat["Sains_Tambahan_Sidang"] > 3]
            if not lebih.empty:
                st.error(f"🚨 {len(lebih)} pusat ST >3 sidang:")
                st.dataframe(lebih, use_container_width=True, hide_index=True)
            else:
                st.success("✅ Semua pusat patuh max 3 sidang ST")
        else:
            st.warning("Data kosong - check file Excel dalam repo")

    elif menu == "Ringkasan Pusat":
        st.subheader("🏫 Ringkasan Pusat Amali (Data LP Rasmi)")
        if not df_ringkasan.empty:
            f1,f2,f3 = st.columns(3)
            with f1:
                kod_list = ["Semua"] + sorted(df_ringkasan["Kod_PPD"].dropna().unique().tolist())
                pilih_ppd = st.selectbox("Tapisan Kod PPD:", kod_list)
            with f2:
                daerah_list = ["Semua"] + sorted(df_ringkasan["Daerah_Asal"].dropna().unique().tolist())
                pilih_daerah = st.selectbox("Tapisan Daerah:", daerah_list)
            with f3:
                pilih_data = st.selectbox("Tapisan Subjek:", ["Semua","Fizik","Kimia","Biologi","Sains Tambahan"])
            df_tapis = df_ringkasan.copy()
            if pilih_ppd != "Semua": df_tapis = df_tapis[df_tapis["Kod_PPD"] == pilih_ppd]
            if pilih_daerah != "Semua": df_tapis = df_tapis[df_tapis["Daerah_Asal"] == pilih_daerah]
            if pilih_data != "Semua":
                col_map = {"Fizik":"Fizik_Sidang","Kimia":"Kimia_Sidang","Biologi":"Biologi_Sidang","Sains Tambahan":"Sains_Tambahan_Sidang"}
                df_tapis = df_tapis[pd.to_numeric(df_tapis[col_map[pilih_data]], errors='coerce') > 0]
            st.markdown(f"<div style='background:#E0F2F1; border:1px solid #00897B; border-radius:8px; padding:8px; font-size:12px;'><b>📊</b> {len(df_tapis)} makmal | {df_tapis['No_Pusat'].nunique()} pusat</div>", unsafe_allow_html=True)
            st.dataframe(df_tapis, use_container_width=True, hide_index=True, height=500)
        else:
            st.info("Data kosong")

    elif menu == "Senarai Makmal Full":
        st.subheader("🏫 Senarai Pusat & Makmal")
        if not df_ringkasan.empty:
            st.dataframe(df_ringkasan, use_container_width=True, hide_index=True, height=600)

    elif menu == "Senarai Sidang":
        st.subheader("📋 Senarai Sidang Detail")
        if not df_full.empty:
            c1,c2 = st.columns(2)
            with c1:
                pilih_sub = st.selectbox("Subjek:", ["Semua","FIZIK","KIMIA","BIOLOGI","SAINS TAMBAHAN"])
            with c2:
                search = st.text_input("Cari No Pusat:", placeholder="BA001")
            df_v = df_full.copy()
            if pilih_sub != "Semua": df_v = df_v[df_v["Subjek"] == pilih_sub]
            if search: df_v = df_v[df_v["No_Pusat"].str.contains(search.upper())]
            st.dataframe(df_v, use_container_width=True, hide_index=True, height=500)
        elif not df_detail.empty:
            st.dataframe(df_detail, use_container_width=True, hide_index=True)

    elif menu == "Analisis":
        st.subheader("📊 Analisis")
        if not df_ringkasan.empty:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Total Sekolah", df_ringkasan["Nama_Sekolah"].nunique())
                st.metric("Total Makmal", len(df_ringkasan))
                st.dataframe(df_ringkasan["Kapasiti_Makmal"].value_counts().reset_index(), use_container_width=True)
            with col_b:
                s_tambahan = df_ringkasan.groupby(["No_Pusat","Nama_Sekolah"])["Sains_Tambahan_Sidang"].sum().reset_index()
                lebih = s_tambahan[s_tambahan["Sains_Tambahan_Sidang"] > 3]
                if not lebih.empty:
                    st.error(f"⚠️ {len(lebih)} pusat ST >3")
                    st.dataframe(lebih)
                else:
                    st.success("✅ Semua patuh")

    elif menu == "Cari Sekolah":
        st.subheader("🔍 Cari Sekolah / Pusat")
        carian = st.text_input("Taip nama / No Pusat / Kod PPD:", placeholder="BA001 atau SMK...")
        if carian and not df_ringkasan.empty:
            df_cari = df_ringkasan[df_ringkasan.apply(lambda row: carian.lower() in str(row.values).lower(), axis=1)]
            st.dataframe(df_cari, use_container_width=True, hide_index=True)
            if not df_cari.empty:
                st.success(f"Ditemui: {df_cari.iloc[0]['Nama_Sekolah']} - {len(df_cari)} makmal")
                if not df_full.empty:
                    pusat = df_cari.iloc[0]['No_Pusat']
                    st.dataframe(df_full[df_full["No_Pusat"] == pusat], use_container_width=True)

    elif menu == "Selenggara Data":
        st.subheader("⚙️ Selenggara Data")
        st.markdown(f"### 📢 Notis Semasa\n{NOTIS_SEMASA}")
        notis_baru = st.text_area("Edit Notis:", value=NOTIS_SEMASA, height=120)
        if st.button("💾 Simpan Notis"):
            if simpan_notis(notis_baru):
                st.success("Disimpan!")
                st.rerun()

st.markdown("---")
st.markdown('<div style="background: linear-gradient(135deg, #004D40 0%, #00695C 100%); border: 2px solid gold; border-radius: 12px; padding: 10px; text-align:center;"><div style="color:gold; font-weight:800; font-size:12px;">© 2026 JPN SELANGOR | DATA LP RASMI 473 MAKMAL</div></div>', unsafe_allow_html=True)
