import streamlit as st

st.set_page_config(page_title="Smart Shopper Calculator", layout="centered")


st.title("🛍️ Is it worth it?")
st.markdown("Compare product sizes, offers, and multipacks to see what's actually worth your 'MONEY, MONEY, MONEY MUST BE FUNNY (No, not funny)'")

st.markdown("---")
st.subheader("📥 Enter Details for Two Products")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Pack 1**")
    price1 = st.number_input("Price of Pack 1 (₹)", min_value=0.0, format="%.2f")
    qty1 = st.number_input("Quantity of Pack 1 (in ml or gm)", min_value=0.0)

    with st.expander("🔁 Got a Deal or Multipack for Pack 1?"):
        deal_qty1 = st.number_input("How many packs in the deal?", min_value=1, value=1, key="deal_qty1")
        deal_price1 = st.number_input("Total deal price for all packs (₹)", min_value=0.0, value=price1, key="deal_price1")

    final_price1 = deal_price1
    final_qty1 = qty1 * deal_qty1

with col2:
    st.markdown("**Pack 2**")
    price2 = st.number_input("Price of Pack 2 (₹)", min_value=0.0, format="%.2f")
    qty2 = st.number_input("Quantity of Pack 2 (in ml or gm)", min_value=0.0)

    with st.expander("🔁 Got a Deal or Multipack for Pack 2?"):
        deal_qty2 = st.number_input("How many packs in the deal?", min_value=1, value=1, key="deal_qty2")
        deal_price2 = st.number_input("Total deal price for all packs (₹)", min_value=0.0, value=price2, key="deal_price2")

    final_price2 = deal_price2
    final_qty2 = qty2 * deal_qty2

st.markdown("---")

if final_qty1 > 0 and final_qty2 > 0:
    unit_price1 = final_price1 / final_qty1
    unit_price2 = final_price2 / final_qty2

    st.subheader("📊 Let's compare!")

    st.write(f"**Pack 1:** ₹{unit_price1:.2f} per unit")
    st.write(f"**Pack 2:** ₹{unit_price2:.2f} per unit")

    if unit_price1 < unit_price2:
        st.success("✅ Pack 1 is totally worth it, queen or king ofc 👑")
    elif unit_price2 < unit_price1:
        st.success("✅ Pack 2 is the smarter buy, no cap 💯")
    else:
        st.info("👯‍♀️ Both are slaying equally — pick your vibe.")

else:
    st.warning("👀 Enter valid quantities to get the tea on which pack is worth it.")
