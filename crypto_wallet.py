import hashlib
import random
import streamlit as st


# --- Wallet Logic ---

def generate_wallet(seed):
    """Generate a private key from a seed."""
    random.seed(seed)
    return random.getrandbits(256)


def generate_public_key(private_key):
    """Derive a public key from the private key using SHA-256."""
    return hashlib.sha256(str(private_key).encode()).hexdigest()


def generate_wallet_address(public_key):
    """Create a wallet address from the public key."""
    wallet_address = hashlib.sha256(public_key.encode()).hexdigest()[:32]
    return "WALLET-" + wallet_address


# --- Session State Setup ---
# Streamlit reruns the script on every interaction, so we use
# session_state to keep values (balance, wallet info) between reruns.

if "balance" not in st.session_state:
    st.session_state.balance = 0.0

if "wallet_address" not in st.session_state:
    seed = 42
    private_key = generate_wallet(seed)
    public_key = generate_public_key(private_key)
    st.session_state.wallet_address = generate_wallet_address(public_key)
    st.session_state.public_key = public_key
    st.session_state.seed = seed

if "message" not in st.session_state:
    st.session_state.message = None   # (text, type) where type is "success" or "error"


# --- Page Config ---

st.set_page_config(page_title="Crypto Wallet", page_icon="💰", layout="centered")
st.title("💰 Crypto Wallet")
st.caption("Simulated blockchain wallet")

st.divider()


# --- Wallet Info ---

st.subheader("Wallet Info")

col1, col2 = st.columns([1, 3])
col1.markdown("**Wallet Address**")
col2.code(st.session_state.wallet_address, language=None)

col1, col2 = st.columns([1, 3])
col1.markdown("**Public Key**")
col2.code(st.session_state.public_key, language=None)

# Generate new wallet button
if st.button("🔄 Generate New Wallet"):
    new_seed = random.randint(0, 999999)
    private_key = generate_wallet(new_seed)
    public_key = generate_public_key(private_key)
    st.session_state.wallet_address = generate_wallet_address(public_key)
    st.session_state.public_key = public_key
    st.session_state.seed = new_seed
    # Reset balance when a new wallet is created
    st.session_state.balance = 0.0
    st.session_state.message = (f"New wallet generated (seed: {new_seed})", "success")
    st.rerun()

st.divider()


# --- Balance ---

st.subheader("Current Balance")
st.metric(label="USD", value=f"${st.session_state.balance:,.2f}", label_visibility="collapsed")

st.divider()


# --- Deposit & Withdraw ---

st.subheader("Deposit / Withdraw")

# Amount input field
amount = st.number_input(
    "Enter amount ($)",
    min_value=0.0,
    step=1.0,
    format="%.2f",
    placeholder="0.00"
)

col_dep, col_with = st.columns(2)

# Deposit button
with col_dep:
    if st.button("✅ Deposit", use_container_width=True):
        if amount <= 0:
            st.session_state.message = ("Please enter an amount greater than zero.", "error")
        else:
            st.session_state.balance += amount
            st.session_state.message = (f"Successfully deposited ${amount:,.2f}.", "success")
        st.rerun()

# Withdraw button
with col_with:
    if st.button("❌ Withdraw", use_container_width=True):
        if amount <= 0:
            st.session_state.message = ("Please enter an amount greater than zero.", "error")
        elif amount > st.session_state.balance:
            st.session_state.message = (
                f"Insufficient funds. Your balance is ${st.session_state.balance:,.2f}.", "error"
            )
        else:
            st.session_state.balance -= amount
            st.session_state.message = (f"Successfully withdrew ${amount:,.2f}.", "success")
        st.rerun()


# --- Status Message ---
# Display success or error feedback after each action

if st.session_state.message:
    text, msg_type = st.session_state.message
    if msg_type == "success":
        st.success(text)
    else:
        st.error(text)