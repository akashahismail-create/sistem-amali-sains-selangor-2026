
import streamlit as st
import os
import pandas as pd
from datetime import datetime, date, timedelta

st.set_page_config(page_title="JPN Selangor - Amali Sains 2026", layout="wide", page_icon="🧪")

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False
if "menu_amali" not in st.session_state:
    st.session_state["menu_amali"] = "Dashboard"

# ===== CSS SPM STYLE - KIRI MENU HIJAU =====
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

/* KIRI MENU BOX - macam SPM */
section.main > div.block-container > div[data-testid="stVerticalBlock"] > div > div[data-testid="stHorizontalBlock"]:nth-child(2) > div[data-testid="column"]:nth-child(1) > div[data-testid="stVerticalBlock"] {{
    background: linear-gradient(180deg, #00695C 0%, #004D40 100%)!important;
    border-radius: 16px!important; padding: 14px!important;
    border: 2px solid #FFD700!important; box-shadow: 0 4px 15px rgba(0,0,0,0.3)!important;
}}

/* BUTTON MENU HIJAU KUNING SPM STYLE */
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
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# COUNTDOWN MALAYSIA
try:
    from zoneinfo import ZoneInfo
    now_my = datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
except:
    now_my = datetime.utcnow() + timedelta(hours=8)
HARI_INI = now_my.date()
TARIKH_AMALI = date(2026, 11, 16)
delta = (TARIKH_AMALI - HARI_INI).days
countdown_num = str(max(delta, 0))

# HERO
st.markdown(f"""
<div class="hero-banner">
    <div style="display:flex; align-items:center;">
        <div style="font-size:45px; margin-right:15px;">🧪</div>
        <div>
            <div class="hero-title">JABATAN PENDIDIKAN SELANGOR</div>
            <div class="hero-subtitle">SEKTOR PENTAKSIRAN DAN PEPERIKSAAN</div>
            <div class="hero-spm">🧪 SIJIL PELAJARAN MALAYSIA 2026 🧪 | SISTEM PENGURUSAN UJIAN AMALI SAINS SELANGOR</div>
            <div style="font-size:10px; color:#FFEB3B; margin-top:4px;">📅 Amali Sains: 16 November 2026 | Hari ini: {HARI_INI.strftime('%d %B %Y')} | {now_my.strftime('%I:%M %p')} MY</div>
        </div>
        <div style="margin-left:auto;">
            <div class="countdown-box" style="background: linear-gradient(135deg, #004D40, #00695C); border:3px solid gold; border-radius:12px; padding:8px 14px; text-align:center; min-width:120px;">
                <div style="color:#FFEB3B; font-size:9px; font-weight:800;">⏳ COUNTDOWN AMALI</div>
                <div style="color:white; font-size:32px; font-weight:900;">{countdown_num}</div>
                <div style="color:gold; font-size:8px; font-weight:700;">HARI LAGI - 16 NOV 2026 (FIZIK)</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SISTEM NOTIS MARQUEE ---
FILE_NOTIS = "pemberitahuan.json"
DEFAULT_NOTIS = "📢 MAKLUMAN TERKINI: SISTEM MASIH DALAM SELENGGARA.MASIH TERDAPAT MAKLUMAT YANG KURANG TEPAT. SEBARANG PERTANYAAN  SILA HUBUNGI SEKTOR PENTAKSIRAN DAN PEPERIKSAAN JPN SELANGOR"

import json

def baca_notis():
    try:
        if os.path.exists(FILE_NOTIS):
            with open(FILE_NOTIS, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "notis" in data:
                    return data["notis"]
                elif isinstance(data, str):
                    return data
        return DEFAULT_NOTIS
    except Exception as e:
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

# CSS Marquee - Pasti keluar
st.markdown("""
<style>
.marquee-container {
    background: linear-gradient(90deg, #B71C1C 0%, #D32F2F 50%, #B71C1C 100%);
    border: 3px solid #FFD700;
    border-radius: 10px;
    padding: 10px 0;
    margin: 10px 0 15px 0;
    overflow: hidden;
    white-space: nowrap;
    box-shadow: 0 4px 15px rgba(183,28,28,0.6);
    position: relative;
    z-index: 999;
}
.marquee-text {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 20s linear infinite;
    color: #FFFFFF;
    font-weight: 900;
    font-size: 15px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: 0.8px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
}
@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
.marquee-container:hover .marquee-text {
    animation-play-state: paused;
}
</style>
""", unsafe_allow_html=True)

# Paparan Marquee - PASTI KELUAR
st.markdown(f"""
<div class="marquee-container">
    <div class="marquee-text">{NOTIS_SEMASA}</div>
</div>
""", unsafe_allow_html=True)

# LOAD DATA - ROBUST + KAPASITI JER
import glob

def cari_file_excel():
    calon_nama = [
        "data_pusat_amali_sains_BETUL.xlsx",
        "Data-Pusat-Amali-Sains-Baru-CLEANED.xlsx",
        "data_pusat_amali_sains_baru_CLEANED.xlsx",
        "DATA_MAKMAL_UJIAN_AMALI_SAINS_SELANGOR.xlsx",
    ]
    semua_xlsx = glob.glob("*.xlsx") + glob.glob("*.XLSX")
    semua_calon = calon_nama + semua_xlsx
    seen = set()
    unique = []
    for f in semua_calon:
        if f not in seen and os.path.exists(f):
            seen.add(f)
            unique.append(f)
    return unique

FILE_EXCEL_CANDIDATES = cari_file_excel()
df_ringkasan = pd.DataFrame()
df_detail = pd.DataFrame()
file_yang_diguna = "TIADA"

for FILE_EXCEL in FILE_EXCEL_CANDIDATES:
    try:
        xls = pd.ExcelFile(FILE_EXCEL)
        if "Ringkasan_Makmal" in xls.sheet_names:
            df_ringkasan = pd.read_excel(FILE_EXCEL, sheet_name="Ringkasan_Makmal")
            df_detail = pd.read_excel(FILE_EXCEL, sheet_name="Data_Pusat_Amali_Sains") if "Data_Pusat_Amali_Sains" in xls.sheet_names else pd.DataFrame()
            file_yang_diguna = FILE_EXCEL
            break
    except:
        continue

if df_ringkasan.empty:
    df_ringkasan = pd.DataFrame([["BD","1","SMK Seksyen 24(2)","Makmal 1",4,4,4,1,90],["BD","1","SMK Seksyen 24(2)","Makmal 2",4,4,4,1,84],["BD","1","SMK Seksyen 24(2)","Makmal 3",4,4,4,1,75]], columns=["Kod_PPD","No_Pusat","Nama_Sekolah","Nama_Makmal","Fizik_Sidang","Kimia_Sidang","Biologi_Sidang","Sains_Tambahan_Sidang","Jumlah_Calon"])
    df_detail = pd.DataFrame()
    file_yang_diguna = "DATA CONTOH"

# KIRAAN: Jumlah Calon = Kapasiti Makmal sahaja (bukan darab)
if not df_ringkasan.empty:
    try:
        for col in ["Fizik_Sidang","Kimia_Sidang","Biologi_Sidang","Sains_Tambahan_Sidang","Jumlah_Calon"]:
            if col not in df_ringkasan.columns:
                df_ringkasan[col] = 0
        for col in ["Fizik_Sidang","Kimia_Sidang","Biologi_Sidang","Sains_Tambahan_Sidang","Jumlah_Calon"]:
            df_ringkasan[col] = pd.to_numeric(df_ringkasan[col], errors='coerce').fillna(0)
        if "Kapasiti_Makmal" not in df_ringkasan.columns:
            df_ringkasan["Kapasiti_Makmal"] = df_ringkasan["Jumlah_Calon"]
        else:
            df_ringkasan["Kapasiti_Makmal"] = pd.to_numeric(df_ringkasan["Kapasiti_Makmal"], errors='coerce').fillna(df_ringkasan["Jumlah_Calon"])
        df_ringkasan["Jumlah_Sidang_Per_Makmal"] = df_ringkasan["Fizik_Sidang"] + df_ringkasan["Kimia_Sidang"] + df_ringkasan["Biologi_Sidang"] + df_ringkasan["Sains_Tambahan_Sidang"]
    except:
        pass

# ===== 2 BAHAGIAN MACAM SPM: KIRI MENU, KANAN CONTENT =====
col_sidebar, col_main = st.columns([1, 4])

with col_sidebar:
    col_t1, col_t2 = st.columns([3,1])
    with col_t1:
        st.markdown("### Menu")
    with col_t2:
        if st.button("🌙" if not st.session_state["dark_mode"] else "☀️", key="dark_toggle"):
            st.session_state["dark_mode"] = not st.session_state["dark_mode"]
            st.rerun()
    
    st.markdown(f"<div style='font-size:11px; color:#FFEB3B; margin-bottom:10px;'>{'🌙 Dark' if st.session_state['dark_mode'] else '☀️ Light'} Mode Amali 2026</div>", unsafe_allow_html=True)
    
    # MENU BARU - Faham Kashah: Dashboard tunjuk Jadual, Senarai Makmal tunjuk KPI Dashboard, tiada butang Jadual
    if st.button("📊 Dashboard", use_container_width=True, key="btn_dashboard_jadual"):
        st.session_state["menu_amali"] = "Dashboard"
    
    if st.button("🏫 Senarai Makmal", use_container_width=True, key="btn_senarai_makmal_kpi"):
        st.session_state["menu_amali"] = "Senarai Makmal"
    
    if st.button("📋 Senarai Sidang", use_container_width=True, key="btn_senarai_sidang"):
        st.session_state["menu_amali"] = "Senarai Sidang"
    if st.button("📊 Analisis", use_container_width=True, key="btn_analisis"):
        st.session_state["menu_amali"] = "Analisis"
    if st.button("🔍 Cari Sekolah", use_container_width=True, key="btn_cari_sekolah"):
        st.session_state["menu_amali"] = "Cari Sekolah"
    if st.button("⚙️ Selenggara Data", use_container_width=True, key="btn_selenggara_data"):
        st.session_state["menu_amali"] = "Selenggara Data"

    st.markdown("---")
    st.link_button("🔙 Kembali ke Dashboard SPM", "https://sistem-jpn-selangor-avpq873obplue8tal3jels.streamlit.app/", use_container_width=True, type="primary")
    st.caption("🔗 SPM Utama")
    st.markdown("---")
    st.markdown(f"<div style='background:#FFF8E1; border:1px solid gold; border-radius:8px; padding:8px; font-size:10px; color:#333;'><b>📦 Spec:</b><br>• 3 Makmal/sekolah<br>• Makmal 1,2,3<br>• Fizik 4 sidang<br>• Kimia 4 sidang<br>• Biologi 4 sidang<br>• Sains Tambahan max 3</div>", unsafe_allow_html=True)

with col_main:
    menu = st.session_state["menu_amali"]
    
    # KPI - JUMLAH CALON = KAPASITI MAKMAL JER (ikut arahan Kashah)
    if not df_ringkasan.empty:
        total_pusat = df_ringkasan["No_Pusat"].nunique()
        total_makmal = len(df_ringkasan)
        try:
            total_sidang = int(df_ringkasan["Jumlah_Sidang_Per_Makmal"].sum()) if "Jumlah_Sidang_Per_Makmal" in df_ringkasan.columns else 0
            total_calon = int(df_ringkasan["Kapasiti_Makmal"].sum()) if "Kapasiti_Makmal" in df_ringkasan.columns else int(df_ringkasan["Jumlah_Calon"].sum())
        except:
            total_sidang = 0
            total_calon = 0
    else:
        total_pusat = 0
        total_makmal = 0
        total_sidang = 0
        total_calon = 0

    # DEBUG FILE
    if "file_yang_diguna" in locals():
        if "CONTOH" in file_yang_diguna or "TIADA" in file_yang_diguna:
            st.error(f"⚠️ File Excel tidak ditemui! Dicari: {FILE_EXCEL_CANDIDATES} | Diguna: {file_yang_diguna}")
        else:
            st.success(f"✅ Data: {file_yang_diguna} | {total_makmal} Makmal | {total_pusat} Pusat | {total_calon} Calon (Kapasiti Makmal Jer)")

    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(f'<div class="kpi-card"><div class="kpi-label">JUMLAH PUSAT AMALI</div><div class="kpi-value">{total_pusat}</div></div>', unsafe_allow_html=True)
    with k2: st.markdown(f'<div class="kpi-card"><div class="kpi-label">JUMLAH MAKMAL (3 PER SEKOLAH)</div><div class="kpi-value">{total_makmal}</div></div>', unsafe_allow_html=True)
    with k3: st.markdown(f'<div class="kpi-card"><div class="kpi-label">JUMLAH SIDANG (4+4+4+MAX3)</div><div class="kpi-value">{total_sidang}</div></div>', unsafe_allow_html=True)
    with k4: st.markdown(f'<div class="kpi-card"><div class="kpi-label">JUMLAH CALON<br><span style="font-size:8px;">Kapasiti Makmal</span></div><div class="kpi-value">{total_calon}</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    if menu == "Dashboard":

        st.subheader("📅 Jadual Ujian Amali Sains SPM 2026")
        
        # TARIKH BESAR
        st.markdown("""
        <div style="display:flex; gap:10px; margin-bottom:15px;">
            <div style="flex:1; background:linear-gradient(135deg, #1565C0, #0D47A1); border:2.5px solid gold; border-radius:12px; padding:12px; text-align:center;">
                <div style="color:#FFEB3B; font-size:11px; font-weight:800;">FIZIK KERTAS 3</div>
                <div style="color:white; font-size:20px; font-weight:900;">16 NOV 2026</div>
                <div style="color:#FFEB3B; font-size:10px;">ISNIN | 4 SIDANG</div>
            </div>
            <div style="flex:1; background:linear-gradient(135deg, #2E7D32, #1B5E20); border:2.5px solid gold; border-radius:12px; padding:12px; text-align:center;">
                <div style="color:#FFEB3B; font-size:11px; font-weight:800;">KIMIA KERTAS 3</div>
                <div style="color:white; font-size:20px; font-weight:900;">17 NOV 2026</div>
                <div style="color:#FFEB3B; font-size:10px;">SELASA | 4 SIDANG</div>
            </div>
            <div style="flex:1; background:linear-gradient(135deg, #6A1B9A, #4A148C); border:2.5px solid gold; border-radius:12px; padding:12px; text-align:center;">
                <div style="color:#FFEB3B; font-size:11px; font-weight:800;">BIOLOGI & SAINS TAMBAHAN KERTAS 3</div>
                <div style="color:white; font-size:20px; font-weight:900;">18 NOV 2026</div>
                <div style="color:#FFEB3B; font-size:10px;">RABU | 4 SIDANG + 3 SIDANG</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔬 Fizik / Kimia / Biologi (4 Sidang)", "🧬 Sains Tambahan Kertas 3 (3 Sidang)"])

        with tab1:
            st.markdown("#### ⏰ Pengurusan Masa - Fizik, Kimia, Biologi")
            st.markdown("*Setiap subjek ada 4 sidang per makmal*")
            
            df_fkb = pd.DataFrame([
                {"Sidang": "SIDANG 1", "Bilik Lapor Diri": "7.30 pagi - 7.45 pagi", "Masa Ujian Makmal": "8.00 am - 8.45 am", "Masa Kuarantin": "8.45 am - 11.45 am"},
                {"Sidang": "SIDANG 2", "Bilik Lapor Diri": "8.45 pagi - 9.00 pagi", "Masa Ujian Makmal": "9.15 am - 10.00 am", "Masa Kuarantin": "10.00 am - 11.45 am"},
                {"Sidang": "SIDANG 3", "Bilik Lapor Diri": "10.30 pagi - 10.45 pagi", "Masa Ujian Makmal": "11.00 am - 11.45 am", "Masa Kuarantin": "TIADA KUARANTIN"},
                {"Sidang": "SIDANG 4", "Bilik Lapor Diri": "11.45 pagi - 12.00 tengah hari", "Masa Ujian Makmal": "12.15 pm - 1.00 tgh", "Masa Kuarantin": "TIADA KUARANTIN"},
            ])
            st.dataframe(df_fkb, use_container_width=True, hide_index=True)
            
            st.markdown("""
            <div style="background:#FFF3E0; border-left:4px solid #FF9800; padding:10px; border-radius:6px; font-size:12px; margin-top:10px;">
            <b>⚠️ Nota Penting Fizik/Kimia/Biologi:</b><br>
            • Calon Sidang 1 & 2 wajib kuarantin sehingga 11.45 pagi<br>
            • Sidang 3 & 4 tiada kuarantin<br>
            • Lapor diri 15 minit sebelum ujian
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("#### ⏰ Pengurusan Masa - Sains Tambahan Kertas 3 (Max 3 Sidang)")
            st.markdown("*Sains Tambahan hanya 3 sidang sahaja per sekolah*")
            
            df_st = pd.DataFrame([
                {"Sidang": "SIDANG 1", "Bilik Lapor Diri": "7.30 - 7.45 pagi", "Masa Ujian": "8.00 - 9.45 pagi (1j 45m)", "Masa Kuarantin": "9.45 am - 1.00 tgh"},
                {"Sidang": "SIDANG 2", "Bilik Lapor Diri": "9.45 - 10.00 pagi", "Masa Ujian": "10.15 - 12.00 tgh (1j 45m)", "Masa Kuarantin": "12.00 - 1.00 tgh"},
                {"Sidang": "SIDANG 3", "Bilik Lapor Diri": "12.00 - 12.15 tgh", "Masa Ujian": "12.30 - 2.15 ptg (1j 45m)", "Masa Kuarantin": "TIADA KUARANTIN"},
            ])
            st.dataframe(df_st, use_container_width=True, hide_index=True)
            
            st.markdown("""
            <div style="background:#E8F5E9; border-left:4px solid #4CAF50; padding:10px; border-radius:6px; font-size:12px; margin-top:10px;">
            <b>✅ Nota Sains Tambahan:</b><br>
            • Maksimum 3 sidang sahaja per sekolah<br>
            • Tempoh ujian 1 jam 45 minit setiap sidang<br>
            • Sidang 1 & 2 ada kuarantin, Sidang 3 tiada kuarantin<br>
            • Contoh SMK Seksyen 24(2): 1 sidang per makmal = total 3 sidang patuh spec
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("#### 📅 Ringkasan Tarikh Rasmi")
        df_ringkas = pd.DataFrame([
            {"Subjek": "Fizik Kertas 3", "Tarikh": "16 November 2026 (Isnin)", "Hari": "16/11/2026", "Sidang": "4 sidang", "Masa": "8.00 am - 1.00 pm"},
            {"Subjek": "Kimia Kertas 3", "Tarikh": "17 November 2026 (Selasa)", "Hari": "17/11/2026", "Sidang": "4 sidang", "Masa": "8.00 am - 1.00 pm"},
            {"Subjek": "Biologi Kertas 3", "Tarikh": "18 November 2026 (Rabu)", "Hari": "18/11/2026", "Sidang": "4 sidang", "Masa": "8.00 am - 1.00 pm"},
            {"Subjek": "Sains Tambahan Kertas 3", "Tarikh": "18 November 2026 (Rabu)", "Hari": "18/11/2026", "Sidang": "Max 3 sidang", "Masa": "8.00 am - 2.15 pm"},
        ])
        st.dataframe(df_ringkas, use_container_width=True, hide_index=True)

    elif menu == "Senarai Makmal":

        st.markdown("#### 📍 Filter Amali Sains")
        f1, f2, f3 = st.columns(3)
        with f1:
            daerah_list = ["Semua Daerah"] + sorted(df_ringkasan["Kod_PPD"].dropna().unique().tolist()) if not df_ringkasan.empty else ["Semua Daerah"]
            pilih_daerah = st.selectbox("📍 Pilih Daerah:", daerah_list, key="filter_daerah_amali")
        with f2:
            pilih_data = st.selectbox("📚 Pilih Data:", ["Semua","Fizik","Kimia","Biologi","Sains Tambahan"], key="filter_data_amali")
        with f3:
            pilih_paparan = st.selectbox("🖥️ Paparan:", ["Semua Data","Ikut Makmal","Ikut Sekolah"], key="filter_paparan")

        df_tapis = df_ringkasan.copy()
        if pilih_daerah != "Semua Daerah" and not df_tapis.empty:
            df_tapis = df_tapis[df_tapis["Kod_PPD"] == pilih_daerah]
        if pilih_data != "Semua" and not df_tapis.empty:
            if pilih_data == "Fizik":
                df_tapis = df_tapis[pd.to_numeric(df_tapis["Fizik_Sidang"], errors='coerce') > 0]
            elif pilih_data == "Kimia":
                df_tapis = df_tapis[pd.to_numeric(df_tapis["Kimia_Sidang"], errors='coerce') > 0]
            elif pilih_data == "Biologi":
                df_tapis = df_tapis[pd.to_numeric(df_tapis["Biologi_Sidang"], errors='coerce') > 0]
            elif pilih_data == "Sains Tambahan":
                df_tapis = df_tapis[pd.to_numeric(df_tapis["Sains_Tambahan_Sidang"], errors='coerce') > 0]

        st.markdown(f"<div style='background:#E0F2F1; border:1px solid #00897B; border-radius:8px; padding:8px; font-size:12px;'><b>📊 Analisis Pantas:</b> Nisbah Sidang : Makmal = {total_sidang/total_makmal:.1f} sidang/makmal | Jumlah Makmal: {total_makmal} | Pusat: {total_pusat}</div>", unsafe_allow_html=True)
        st.write("")
        st.dataframe(df_tapis, use_container_width=True, hide_index=True, height=400)


    elif menu == "Senarai Makmal Full":

        st.subheader("🏫 Senarai Pusat & Makmal (3 Makmal per Sekolah)")
        st.markdown("*Setiap sekolah: Makmal 1, Makmal 2, Makmal 3 | Setiap makmal: Fizik 4, Kimia 4, Biologi 4 sidang | Sains Tambahan max 3 sidang per sekolah*")
        st.dataframe(df_ringkasan, use_container_width=True, hide_index=True)

    elif menu == "Senarai Sidang":
        st.subheader("📋 Senarai Sidang Detail")
        st.markdown("**Peraturan: Fizik 4 sidang, Kimia 4 sidang, Biologi 4 sidang, Sains Tambahan maksimum 3 sidang sahaja**")
        if not df_detail.empty:
            c1,c2 = st.columns(2)
            with c1:
                sek = ["Semua"] + sorted(df_detail["Nama_Sekolah"].dropna().unique().tolist())
                pilih_s = st.selectbox("Pilih Sekolah:", sek, key="sidang_sekolah")
            with c2:
                pilih_sub = st.selectbox("Pilih Subjek:", ["Semua","Fizik","Kimia","Biologi","Sains Tambahan"], key="sidang_subjek")
            df_v = df_detail.copy()
            if pilih_s != "Semua": df_v = df_v[df_v["Nama_Sekolah"] == pilih_s]
            if pilih_sub != "Semua": df_v = df_v[df_v["Subjek"] == pilih_sub]
            st.dataframe(df_v, use_container_width=True, hide_index=True)
        else:
            st.info("Data detail kosong - data contoh dalam Ringkasan_Makmal sudah ada 3 makmal x 4 subjek")

    elif menu == "Analisis":
        st.subheader("📊 Analisis Amali Sains")
        if not df_ringkasan.empty:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Total Sekolah", df_ringkasan["Nama_Sekolah"].nunique())
                st.metric("Total Makmal", len(df_ringkasan))
                st.metric("Avg Makmal/Sekolah", f"{len(df_ringkasan)/df_ringkasan['Nama_Sekolah'].nunique():.1f} (target 3.0)")
            with col_b:
                try:
                    s_tambahan = df_ringkasan.groupby("Nama_Sekolah")["Sains_Tambahan_Sidang"].apply(lambda x: pd.to_numeric(x, errors='coerce').sum())
                    st.write("**Sains Tambahan per Sekolah (max 3):**")
                    st.dataframe(s_tambahan)
                    lebih = s_tambahan[s_tambahan > 3]
                    if not lebih.empty:
                        st.error(f"⚠️ {len(lebih)} sekolah lebih 3 sidang Sains Tambahan!")
                    else:
                        st.success("✅ Semua sekolah patuh max 3 sidang Sains Tambahan")
                except Exception as e:
                    st.error(str(e))

    elif menu == "Cari Sekolah":
        st.subheader("🔍 Cari Sekolah Amali")
        carian = st.text_input("Taip nama sekolah / No Pusat / Kod PPD:", placeholder="Contoh: SMK Seksyen 24(2) atau BD atau 1")
        if carian and not df_ringkasan.empty:
            df_cari = df_ringkasan[df_ringkasan.apply(lambda row: carian.lower() in str(row.values).lower(), axis=1)]
            st.dataframe(df_cari, use_container_width=True, hide_index=True)
            if not df_cari.empty:
                st.success(f"Ditemui: {df_cari.iloc[0]['Nama_Sekolah']} - {len(df_cari)} makmal (Makmal 1,2,3)")

    elif menu == "Selenggara Data":
        st.subheader("⚙️ Selenggara Data Amali Sains")
        
        # --- EDITOR NOTIS MARQUEE ---
        st.markdown("### 📢 Sistem Notis Marquee - Edit Teks Berjalan")
        st.markdown(f"""
        <div style="background:#FFEBEE; border:2.5px solid #D32F2F; border-radius:10px; padding:12px; margin-bottom:12px;">
        <b style="color:#B71C1C;">📢 Notis Semasa (sedang berjalan):</b><br>
        <span style="color:#D32F2F; font-weight:bold; font-size:13px;">{NOTIS_SEMASA}</span>
        </div>
        """, unsafe_allow_html=True)
        
        notis_baru = st.text_area("✏️ Edit Teks Notis Marquee:", value=NOTIS_SEMASA, height=120, key="edit_notis_marquee")
        col_n1, col_n2, col_n3 = st.columns([1,1,1])
        with col_n1:
            if st.button("💾 Simpan Notis", use_container_width=True, key="btn_simpan_notis_final"):
                if simpan_notis(notis_baru):
                    st.success("✅ Notis berjaya disimpan! Marquee akan update.")
                    st.rerun()
        with col_n2:
            if st.button("🔄 Reset Default", use_container_width=True, key="btn_reset_notis_final"):
                if simpan_notis(DEFAULT_NOTIS):
                    st.success("✅ Notis reset ke default!")
                    st.rerun()
        with col_n3:
            if st.button("👁️ Preview", use_container_width=True, key="btn_preview_notis"):
                st.markdown(f"""
                <div style="background:#B71C1C; border:2px solid gold; border-radius:8px; padding:8px; margin-top:8px;">
                <marquee style="color:white; font-weight:bold;">{notis_baru}</marquee>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.info("Modul selenggara - Upload Excel baru 3 makmal 4 sidang")
        uploaded = st.file_uploader("Upload Excel Amali Sains Baru", type=["xlsx"])
        if uploaded:
            try:
                df_new = pd.read_excel(uploaded, sheet_name="Ringkasan_Makmal")
                st.success(f"Berjaya baca {len(df_new)} makmal")
                st.dataframe(df_new.head())
                if st.button("💾 Simpan ke data_pusat_amali_sains_BETUL.xlsx"):
                    with pd.ExcelWriter(FILE_EXCEL, engine='openpyxl') as writer:
                        df_new.to_excel(writer, sheet_name="Ringkasan_Makmal", index=False)
                    st.success("Disimpan! Sila refresh page")
            except Exception as e:
                st.error(f"Error: {e}")

# FOOTER
st.markdown("---")
st.markdown('<div style="background: linear-gradient(135deg, #004D40 0%, #00695C 100%); border: 2px solid gold; border-radius: 12px; padding: 10px; text-align:center;"><div style="color:gold; font-weight:800; font-size:12px;">© 2026 JPN SELANGOR | SEKTOR PENTAKSIRAN DAN PEPERIKSAAN | UJIAN AMALI SAINS 2026</div><div style="color:white; font-size:11px; margin-top:4px;">3 Makmal per Sekolah (Makmal 1,2,3) | Fizik 4 | Kimia 4 | Biologi 4 | Sains Tambahan max 3 | Dashboard 2 Bahagian Kiri Menu</div></div>', unsafe_allow_html=True)
