
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
def load_data():
    return pd.read_csv("C:\\Users\\ayxnk\\Desktop\\Renewable_Energy_Analysis\\data\\renewable_energy.csv")

df = load_data()

# Streamlit app
st.set_page_config(page_title="Renewable Energy Analysis", layout="wide")
st.title("🌍 Renewable Energy Production Analysis")

# Sidebar filters
country = st.sidebar.selectbox("Select Country", df["Country"].unique())
energy_source = st.sidebar.selectbox("Select Energy Source", ["Solar", "Wind", "Hydro"])

# Filter data
filtered_df = df[(df["Country"] == country) & (df["Energy Source"] == energy_source)]

# Line chart for energy production over years
fig = px.line(filtered_df, x="Year", y="Production (TWh)", 
              title=f"{energy_source} Production in {country}", markers=True)
st.plotly_chart(fig, use_container_width=True)

# Dynamic Explanation Based on Selected Country and Energy Source
st.markdown("## 📊 Graph Explanation")

st.markdown("""
### **1️⃣ If the Line Goes Up 📈 (Increasing Trend)**
- **Renewable energy production is growing** in the selected country for that energy source.  
- Possible reasons:
  - Government incentives for renewable energy.
  - Increased investment in solar, wind, or hydroelectric plants.
  - Technological advancements making renewables more efficient.

### **2️⃣ If the Line Goes Down 📉 (Decreasing Trend)**
- The country **reduced** its production of this energy source.  
- Possible reasons:
  - Shift in policy (e.g., cutting subsidies for renewables).
  - Economic crisis affecting investments in energy infrastructure.
  - Environmental factors (e.g., drought affecting hydroelectric power).

### **3️⃣ If the Line Fluctuates 🔄 (Up and Down)**
- The production varies due to **seasonal changes** or **policy shifts**.  
- Examples:
  - **Wind power** varies depending on seasonal winds.
  - **Solar power** is affected by sunshine hours.
  - **Hydropower** depends on rainfall and water availability.
  """)
  
st.markdown("## 📊 Country & Energy Source Analysis")

def get_explanation(country, energy_source):
    explanations = {
        "India": {
            "Solar": """### 🌞 **India's Solar Energy Boom**
- **Why?** India has **abundant sunlight** (300+ sunny days a year) and a strong push from the government.
- **Projects:** **Bhadla Solar Park** (World’s largest), **Rewa Solar Plant**.
- **Challenges:** Land scarcity, expensive storage solutions.
- **Future:** **500 GW of renewable energy by 2030**.
            """,
            "Wind": """### 🌬️ **India's Wind Power Growth**
- **Why?** Strong coastal winds in **Tamil Nadu, Gujarat, Maharashtra**.
- **Projects:** **Muppandal Wind Farm** (Asia’s largest).
- **Challenges:** Unstable wind patterns.
- **Future:** **Expanding offshore wind farms** in **Gujarat & Tamil Nadu**.
            """,
            "Hydro": """### 💧 **India's Hydropower Strength**
- **Why?** Himalayan rivers offer **huge potential**.
- **Projects:** **Tehri Dam, Bhakra Nangal Dam**.
- **Challenges:** Monsoon dependency, displacement of people.
- **Future:** **Small hydropower plants** for sustainability.
            """
        },
        "USA": {
            "Solar": """### 🌞 **USA’s Solar Expansion**
- **Why?** **80% cost reduction** in the last decade.
- **Hotspots:** **California, Texas, Arizona**.
- **Projects:** **Topaz Solar Farm (550 MW), Desert Sunlight Solar Farm**.
- **Challenges:** Dependence on subsidies.
- **Future:** **100% clean energy target by 2050**.
            """,
            "Wind": """### 🌬️ **USA’s Wind Power Leadership**
- **Why?** **Great Plains (Texas, Iowa, Oklahoma)** have strong winds.
- **Projects:** **Roscoe Wind Farm, Alta Wind Energy Center**.
- **Challenges:** **Bird migration impact**.
- **Future:** **More offshore wind farms in New York & Massachusetts**.
            """,
            "Hydro": """### 💧 **USA's Hydropower**
- **Why?** **6-7% of total electricity** from hydropower.
- **Projects:** **Grand Coulee Dam, Hoover Dam**.
- **Challenges:** **Climate change reducing water levels**.
- **Future:** **Modernizing old dams** for efficiency.
            """
        },
        "China": {
            "Solar": """### 🌞 **China: The Solar Giant**
- **Why?** **Mass production of solar panels** + government support.
- **Projects:** **Tengger Desert Solar Park, Datong Solar Power Plant**.
- **Challenges:** **Air pollution reducing efficiency**.
- **Future:** **Floating solar farms** on lakes.
            """,
            "Wind": """### 🌬️ **China’s Wind Power Boom**
- **Why?** **Vast land in Inner Mongolia & coastal areas**.
- **Projects:** **Gansu Wind Farm** (World’s largest).
- **Challenges:** **Grid connectivity issues**.
- **Future:** **1,200 GW wind energy target by 2030**.
            """,
            "Hydro": """### 💧 **China’s Hydropower Mega Projects**
- **Why?** **Rivers like the Yangtze & Yellow River**.
- **Projects:** **Three Gorges Dam** (World’s largest).
- **Challenges:** **Displacing millions of people**.
- **Future:** **More efficient dam technology**.
            """
        },
        "UK": {
            "Solar": """### 🌞 **UK’s Growing Solar Market**
- **Why?** **Despite cloudy weather, solar is expanding**.
- **Projects:** **Shotwick Solar Park, Westmill Solar Co-operative**.
- **Challenges:** **Weather dependency**.
- **Future:** **More home solar panels & battery storage incentives**.
            """,
            "Wind": """### 🌬️ **UK’s Offshore Wind Energy**
- **Why?** **Strong North Sea winds**.
- **Projects:** **Dogger Bank Wind Farm** (World’s biggest offshore wind farm).
- **Challenges:** **High maintenance costs**.
- **Future:** Wind is set to provide **50% of UK’s electricity by 2030**.
            """,
            "Hydro": """### 💧 **UK’s Hydropower Industry**
- **Why?** **Rivers in Scotland & Wales** offer potential.
- **Projects:** **Loch Sloy Hydroelectric Scheme, Dinorwig Power Station**.
- **Challenges:** **Limited large-scale expansion potential**.
- **Future:** **Focus on small hydro plants**.
            """
        },
        "France": {
            "Solar": """### 🌞 **France’s Solar Energy Growth**
- **Why?** **Government incentives & European Union policies**.
- **Projects:** **Cestas Solar Park (300 MW)**.
- **Challenges:** **Land availability**.
- **Future:** **Doubling solar capacity by 2035**.
            """,
            "Wind": """### 🌬️ **France’s Wind Power**
- **Why?** **High potential in Northern France**.
- **Projects:** **Saint-Nazaire Offshore Wind Farm**.
- **Challenges:** **Opposition from local communities**.
- **Future:** **More offshore wind development**.
            """,
            "Hydro": """### 💧 **France’s Alpine Hydropower**
- **Why?** **Mountainous rivers in the Alps & Pyrenees**.
- **Projects:** **Serre-Ponçon Dam, Génissiat Dam**.
- **Challenges:** **Environmental regulations**.
- **Future:** **Small-scale hydro plants** for sustainability.
            """
        },
        "Brazil": {
            "Solar": """### 🌞 **Brazil’s Solar Expansion**
- **Why?** **High solar radiation year-round**.
- **Projects:** **Pirapora Solar Complex**.
- **Challenges:** **Grid integration issues**.
- **Future:** **Expanding decentralized solar power**.
            """,
            "Wind": """### 🌬️ **Brazil’s Wind Energy**
- **Why?** **Strong Atlantic coast winds**.
- **Projects:** **Osório Wind Complex**.
- **Challenges:** **Transmission network expansion**.
- **Future:** **Massive offshore wind projects planned**.
            """,
            "Hydro": """### 💧 **Brazil’s Amazon Hydropower**
- **Why?** **Amazon River provides huge potential**.
- **Projects:** **Itaipu Dam, Belo Monte Dam**.
- **Challenges:** **Deforestation & indigenous displacement**.
- **Future:** **Sustainable hydro projects with better planning**.
            """
        },
            "Australia": {
        "Solar": """### 🌞 **Australia’s Solar Boom**
- **Why?** **One of the sunniest countries in the world**.
- **Projects:** **Nyngan Solar Plant, Broken Hill Solar Plant**.
- **Challenges:** **Grid congestion, storage issues**.
- **Future:** **More battery storage & solar farms in deserts**.
        """,
        "Wind": """### 🌬️ **Australia’s Wind Power Expansion**
- **Why?** **Strong coastal & inland winds**.
- **Projects:** **Macarthur Wind Farm, Snowtown Wind Farm**.
- **Challenges:** **Distance from urban centers**.
- **Future:** **Developing offshore wind farms**.
        """,
        "Hydro": """### 💧 **Australia’s Hydropower Industry**
- **Why?** **Mountainous terrain with seasonal rainfall**.
- **Projects:** **Snowy Mountains Hydroelectric Scheme**.
- **Challenges:** **Drought & climate change impact**.
- **Future:** **More pumped hydro storage projects**.
        """
    },
    "Canada": {
        "Solar": """### 🌞 **Canada’s Solar Potential**
- **Why?** **Best in Alberta & Ontario**.
- **Projects:** **Claresholm Solar Project, Kingston Solar Project**.
- **Challenges:** **Less sunlight in winter**.
- **Future:** **Advancements in winter solar tech**.
        """,
        "Wind": """### 🌬️ **Canada’s Wind Energy Growth**
- **Why?** **Strong winds in the prairies & coastal regions**.
- **Projects:** **Ontario & Quebec Wind Farms**.
- **Challenges:** **Cold weather maintenance**.
- **Future:** **More offshore wind expansion in Atlantic Canada**.
        """,
        "Hydro": """### 💧 **Canada’s Hydropower Strength**
- **Why?** **Massive water resources**.
- **Projects:** **James Bay Project, Churchill Falls**.
- **Challenges:** **Indigenous land disputes**.
- **Future:** **Sustainable hydro projects**.
        """
    },
    "Japan": {
        "Solar": """### 🌞 **Japan’s Solar Energy**
- **Why?** **Government support after Fukushima disaster**.
- **Projects:** **Kagoshima Solar Power Plant**.
- **Challenges:** **Limited land for large-scale farms**.
- **Future:** **Floating solar plants on lakes & reservoirs**.
        """,
        "Wind": """### 🌬️ **Japan’s Wind Energy Growth**
- **Why?** **Coastal winds & typhoon-resistant tech**.
- **Projects:** **Akita Offshore Wind Farm**.
- **Challenges:** **Earthquake risks for turbines**.
- **Future:** **More offshore floating wind farms**.
        """,
        "Hydro": """### 💧 **Japan’s Hydropower Usage**
- **Why?** **Mountainous terrain ideal for hydro**.
- **Projects:** **Kurobe Dam, Hida Hydroelectric Stations**.
- **Challenges:** **Environmental concerns**.
- **Future:** **Small-scale hydro plants for sustainability**.
        """
        },
    "Japan": {
        "Solar": """### 🌞 **France’s Solar Power Development**
- **Why?** **Government incentives & EU renewable targets**.
- **Projects:** **Cestas Solar Park (largest in France)**.
- **Challenges:** **Less sunlight in northern France**.
- **Future:** **More rooftop solar & agrivoltaics (solar farms on farmland)**.
    """,
    "Wind": """### 🌬️ **France’s Wind Energy Expansion**
- **Why?** **Strong winds in coastal regions (Brittany, Normandy)**.
- **Projects:** **Fécamp & Saint-Nazaire Offshore Wind Farms**.
- **Challenges:** **Public opposition due to landscape impact**.
- **Future:** **More offshore wind development in the Mediterranean**.
    """,
    "Hydro": """### 💧 **France’s Hydropower Strength**
- **Why?** **Mountainous terrain (Alps, Pyrenees) & large rivers**.
- **Projects:** **Grand'Maison Dam (biggest hydro plant in France)**.
- **Challenges:** **Aging infrastructure needing upgrades**.
- **Future:** **Modernization of dams for efficiency & pumped-storage projects**.
    """
    }
}
    
    return explanations.get(country, {}).get(energy_source, "No specific data available for this selection.")

# Show explanation based on selection
st.markdown(f"### **{energy_source} Energy in {country}**")
st.markdown(get_explanation(country, energy_source))

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
