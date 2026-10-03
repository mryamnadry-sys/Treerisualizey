import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# تنظیمات اصلی سایت
st.set_page_config(page_title="آموزش هوشمند درخت", layout="wide")

# استایل‌بندی سفارشی برای زیبایی بیشتر
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4CAF50; color: white; font-weight: bold; }
    .stSuccess { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌳 آزمایشگاه هوشمندِ ساختارِ داده")
st.write("در اینجا ما یاد می‌گیریم چطور کامپیوترها در دلِ یک درختِ داده سفر می‌کنند.")

# تابع رسم درخت (برای زیبایی بیشتر، بک‌گراند را شفاف کردیم)
def draw_tree():
    G = nx.Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    G.add_edges_from(edges)
    pos = {1: (0, 3), 2: (-2, 1), 3: (2, 1), 4: (-3, -1), 5: (-1, -1), 6: (1, -1), 7: (3, -1)}
    
    fig, ax = plt.subplots(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='#ffcc00', node_size=1500, 
            font_size=15, font_weight='bold', edge_color='#555', ax=ax)
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    st.pyplot(fig)

# منطق پیمایش‌ها
traversals = {
    "پیش‌تریب (Pre-order)": {"path": [1, 2, 4, 5, 3, 6, 7], "desc": "قانونِ رئیس: اول ریشه، بعد چپ، بعد راست."},
    "میان‌تریب (In-order)": {"path": [4, 2, 5, 1, 6, 3, 7], "desc": "قانونِ قد: اول چپ، بعد ریشه، بعد راست."},
    "پس‌تریب (Post-order)": {"path": [4, 5, 2, 6, 7, 3, 1], "desc": "قانونِ خانه‌تکانی: اول چپ، بعد راست، در آخر ریشه."},
    "سطح (Level-order)": {"path": [1, 2, 3, 4, 5, 6, 7], "desc": "قانونِ عکس: ردیف به ردیف از بالا به پایین."}
}

# چیدمان ستونی برای زیبایی
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("انتخاب مسیر سفر")
    selected = st.radio("نوع پیمایش را انتخاب کن:", list(traversals.keys()))
    
    st.divider()
    
    # نمایش نتیجه
    res = traversals[selected]
    st.success(f"ترتیب بازدید: {res['path']}")
    st.info(f"💡 {res['desc']}")

with col2:
    st.subheader("نمای درختی")
    draw_tree()

st.divider()
st.caption("طراحی شده با عشق برای یادگیری بهتر | پروژه آموزشی داده‌ساختار")
