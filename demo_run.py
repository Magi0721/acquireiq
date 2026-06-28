"""
AcquireIQ - DEMO MODE (No API key needed)
Run this to see the full pipeline with realistic pre-built outputs.
Perfect for video recording and testing the UI.

Usage: python demo_run.py
"""

import time
import sys

# ── ANSI colors (no external libraries needed) ───────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
MAGENTA= "\033[95m"
BLUE   = "\033[94m"
WHITE  = "\033[97m"
BG_DARK= "\033[40m"

def box(text, color=CYAN, width=70):
    line = "─" * width
    print(f"{color}┌{line}┐{RESET}")
    for t in text if isinstance(text, list) else [text]:
        pad = width - len(t)
        print(f"{color}│{RESET} {BOLD}{t}{RESET}{' ' * (pad-1)}{color}│{RESET}")
    print(f"{color}└{line}┘{RESET}")

def panel(title, content, color=WHITE, border=CYAN):
    width = 68
    print(f"\n{border}╔{'═'*width}╗{RESET}")
    pad = width - len(title) - 2
    print(f"{border}║{RESET} {BOLD}{color}{title}{RESET}{' '*pad}{border}║{RESET}")
    print(f"{border}╠{'═'*width}╣{RESET}")
    for line in content:
        pad = width - len(line) - 1
        print(f"{border}║{RESET} {line}{' '*max(0,pad)}{border}║{RESET}")
    print(f"{border}╚{'═'*width}╝{RESET}")

def spinner(msg, seconds=1.2):
    chars = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {CYAN}{chars[i % len(chars)]}{RESET} {DIM}{msg}...{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r  {GREEN}✓{RESET} {msg}       \n")

def hr(label="", color=CYAN):
    if label:
        pad = (66 - len(label)) // 2
        print(f"\n{color}{'─'*pad} {BOLD}{label}{RESET}{color} {'─'*(66-pad-len(label))}─{RESET}\n")
    else:
        print(f"\n{color}{'─'*70}{RESET}\n")

# ── Demo Data ─────────────────────────────────────────────────────────────────
PROSPECTS = [
    {
        "id": "A1B2C3",
        "name": "Arjun Sharma",
        "location": "Lucknow, Uttar Pradesh",
        "tier": "Tier-2",
        "segment": "MSME Owner",
        "signal": "New Pvt Ltd registered on MCA21 — Textile trading, ₹8L capital",
        "language": "Hindi",
        "score": 88,
        "health": "Medium",
        "product": "MSME Loan",
        "reasoning": "Fresh business registration with declared capital signals immediate need for working capital and a current account.",
        "channel": "WHATSAPP",
        "send_time": "10:30 AM",
        "message": (
            "नमस्ते अर्जुन जी! 🙏\n"
            "आपके नए टेक्सटाइल व्यापार के लिए बधाई!\n"
            "SBI का MSME लोन आपके बिज़नेस को आगे बढ़ाने में\n"
            "मदद कर सकता है — कम ब्याज दर, आसान प्रक्रिया।\n"
            "नज़दीकी SBI शाखा में आएं या 1800 1234 पर कॉल करें।\n"
            "Reply STOP to opt out."
        ),
        "compliance": True,
        "action": "ESCALATE TO RM",
        "escalate": True,
        "escalate_msg": (
            "🔴 HOT LEAD — Score 88/100\n"
            "Prospect: Arjun Sharma, Lucknow\n"
            "Product: MSME Loan\n"
            "Signal: MCA21 new business registration\n"
            "Action: Personal call within 2 hours"
        ),
    },
    {
        "id": "D4E5F6",
        "name": "Priya Nair",
        "location": "Coimbatore, Tamil Nadu",
        "tier": "Tier-2",
        "segment": "Home Seeker",
        "signal": "Active property search on MagicBricks — 3BHK, viewed 14 listings",
        "language": "Tamil",
        "score": 76,
        "health": "High",
        "product": "Home Loan",
        "reasoning": "High-frequency property portal activity combined with tier-2 location indicates strong home loan intent.",
        "channel": "WHATSAPP",
        "send_time": "07:30 PM",
        "message": (
            "வணக்கம் பிரியா! 🏠\n"
            "புதிய வீடு தேடுகிறீர்களா?\n"
            "SBI Home Loan — குறைந்த வட்டி விகிதம்,\n"
            "எளிதான ஆவண செயல்முறை.\n"
            "அருகிலுள்ள SBI கிளையை பார்வையிடுங்கள்.\n"
            "Reply STOP to opt out."
        ),
        "compliance": True,
        "action": "ADAPTIVE FOLLOW-UP",
        "escalate": False,
        "escalate_msg": (
            "Score 76 — warm lead. Send follow-up in 48 hours\n"
            "with EMI calculator offer to increase engagement."
        ),
    },
    {
        "id": "G7H8I9",
        "name": "Sunita Devi",
        "location": "Varanasi, Uttar Pradesh",
        "tier": "Tier-3",
        "segment": "Rural / Unbanked",
        "signal": "Agricultural district resident — no formal banking footprint detected",
        "language": "Hindi",
        "score": 82,
        "health": "Low",
        "product": "Jan Dhan Account",
        "reasoning": "Rural resident with zero banking footprint — highest priority for SBI financial inclusion mandate, Jan Dhan directly applicable.",
        "channel": "SMS",
        "send_time": "06:30 AM",
        "message": (
            "नमस्ते सुनीता जी!\n"
            "SBI जन धन खाता खोलें — बिल्कुल मुफ्त!\n"
            "₹10,000 ओवरड्राफ्ट + RuPay कार्ड + बीमा।\n"
            "नज़दीकी SBI शाखा जाएं, आधार लेकर आएं।\n"
            "Reply STOP to opt out."
        ),
        "compliance": True,
        "action": "ESCALATE TO RM",
        "escalate": True,
        "escalate_msg": (
            "🔴 HOT LEAD — Score 82/100\n"
            "Prospect: Sunita Devi, Varanasi (Rural)\n"
            "Product: Jan Dhan Account\n"
            "Signal: Zero banking footprint — financial inclusion priority\n"
            "Action: Assign to rural outreach RM immediately"
        ),
    },
]

# ── Main Demo ─────────────────────────────────────────────────────────────────
def main():
    print("\n" * 2)

    # Banner
    print(f"{CYAN}{'═'*70}{RESET}")
    print(f"{BOLD}{CYAN}  █████╗  ██████╗ ██████╗ ██╗   ██╗██╗██████╗ ███████╗{RESET}    {DIM}IQ{RESET}")
    print(f"{CYAN}  ██╔══██╗██╔════╝██╔═══██╗██║   ██║██║██╔══██╗██╔════╝{RESET}")
    print(f"{CYAN}  ███████║██║     ██║   ██║██║   ██║██║██████╔╝█████╗  {RESET}")
    print(f"{CYAN}  ██╔══██║██║     ██║▄▄ ██║██║   ██║██║██╔══██╗██╔══╝  {RESET}")
    print(f"{CYAN}  ██║  ██║╚██████╗╚██████╔╝╚██████╔╝██║██║  ██║███████╗{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}")
    print(f"  {WHITE}Agentic AI for Intelligent Bank Customer Acquisition{RESET}")
    print(f"  {DIM}SBI Hackathon 2025 · Theme: Agentic AI & Emerging Tech{RESET}")
    print(f"  {DIM}Built by: Magi Vaishnavi S{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}\n")

    time.sleep(1)

    # Pipeline overview
    print(f"{BOLD}  PIPELINE:{RESET}")
    steps = [
        ("1", "Discovery Agent", "Finds high-intent prospects from public data"),
        ("2", "Profiling Agent",  "Scores leads + matches SBI product via LLM"),
        ("3", "Outreach Agent",   "Generates multilingual personalized messages"),
        ("4", "Nurture Agent",    "Follow-up, objection handling, RM escalation"),
    ]
    for num, name, desc in steps:
        print(f"  {CYAN}[{num}]{RESET} {BOLD}{name:<22}{RESET} {DIM}{desc}{RESET}")

    print(f"\n  {DIM}RBI Compliance Guard runs at every outreach step{RESET}")
    time.sleep(1.5)

    # ── STAGE 1: Discovery ────────────────────────────────────────────────────
    hr("AGENT 1 — DISCOVERY", BLUE)
    print(f"  {DIM}Scanning public sources for high-intent signals...{RESET}\n")

    sources = [
        ("MCA21 Portal",       "New business registrations"),
        ("RERA Database",      "Active property searches"),
        ("Job Portals",        "New employment signals"),
        ("Geographic Filter",  "Tier-2/3 city prioritization"),
    ]
    for src, desc in sources:
        spinner(f"{src} — {desc}", 0.7)

    print(f"\n  {GREEN}✓ {BOLD}3 high-intent prospects discovered{RESET}\n")

    for p in PROSPECTS:
        tier_color = YELLOW if p["tier"] == "Tier-2" else RED
        print(f"  {CYAN}●{RESET} {BOLD}{p['name']}{RESET} · {p['location']} "
              f"[{tier_color}{p['tier']}{RESET}]")
        print(f"    {DIM}{p['signal']}{RESET}")

    time.sleep(1)

    # ── Process each prospect ─────────────────────────────────────────────────
    for i, p in enumerate(PROSPECTS, 1):

        hr(f"PROSPECT {i}/3 — {p['name'].upper()}", CYAN)

        # Prospect card
        print(f"  {BOLD}Name:{RESET}     {p['name']}")
        print(f"  {BOLD}Location:{RESET} {p['location']} ({p['tier']})")
        print(f"  {BOLD}Segment:{RESET}  {p['segment']}")
        print(f"  {BOLD}Signal:{RESET}   {DIM}{p['signal']}{RESET}\n")
        time.sleep(0.5)

        # Stage 2: Profiling
        print(f"{YELLOW}  📊 AGENT 2 — PROFILING AGENT{RESET}")
        spinner("Running LLM lead scoring", 1.4)
        spinner("Estimating financial health", 0.9)
        spinner("Matching best SBI product", 0.8)

        score = p["score"]
        score_color = GREEN if score >= 80 else YELLOW if score >= 60 else RED
        bar_filled = int(score / 5)
        bar = f"{'█' * bar_filled}{'░' * (20 - bar_filled)}"

        print(f"\n  {BOLD}Lead Score:{RESET}  [{score_color}{bar}{RESET}] "
              f"{score_color}{BOLD}{score}/100{RESET}")
        print(f"  {BOLD}Product:{RESET}     {GREEN}{p['product']}{RESET}")
        print(f"  {BOLD}Fin. Health:{RESET} {p['health']}")
        print(f"  {BOLD}Reasoning:{RESET}   {DIM}{p['reasoning']}{RESET}\n")
        time.sleep(0.8)

        # Stage 3: Outreach
        print(f"{MAGENTA}  💬 AGENT 3 — OUTREACH AGENT{RESET}")
        spinner(f"Selecting channel ({p['channel']})", 0.7)
        spinner(f"Generating message in {p['language']}", 1.5)
        spinner("Calculating optimal send time", 0.6)

        print(f"\n  {BOLD}Channel:{RESET}   {MAGENTA}{p['channel']}{RESET} "
              f"({p['language']})")
        print(f"  {BOLD}Send at:{RESET}   {p['send_time']}")
        print()
        print(f"  {MAGENTA}┌{'─'*56}┐{RESET}")
        print(f"  {MAGENTA}│{RESET}  {BOLD}Generated Message{RESET}"
              f"{'':>38}{MAGENTA}│{RESET}")
        print(f"  {MAGENTA}├{'─'*56}┤{RESET}")
        for line in p["message"].split("\n"):
            pad = 56 - len(line) - 2
            print(f"  {MAGENTA}│{RESET}  {line}{' '*max(0,pad)}{MAGENTA}│{RESET}")
        print(f"  {MAGENTA}└{'─'*56}┘{RESET}\n")
        time.sleep(0.5)

        # Compliance
        if p["compliance"]:
            print(f"  {GREEN}🛡  RBI Compliance: ✅ PASSED{RESET}")
            print(f"  {DIM}    ✓ No banned phrases  ✓ TRAI window OK  "
                  f"✓ Opt-out present{RESET}\n")
        else:
            print(f"  {RED}🛡  RBI Compliance: ❌ FAILED — Message blocked{RESET}\n")

        time.sleep(0.6)

        # Stage 4: Nurture
        print(f"{GREEN}  🔁 AGENT 4 — NURTURE AGENT{RESET}")
        spinner("Analyzing lead score + response signals", 1.0)
        spinner("Deciding next action", 0.7)

        action_color = RED if p["escalate"] else YELLOW
        print(f"\n  {BOLD}Action:{RESET}  [{action_color}{p['action']}{RESET}]")
        print()

        if p["escalate"]:
            print(f"  {RED}╔{'═'*56}╗{RESET}")
            print(f"  {RED}║{RESET}  {BOLD}{RED}🔴 RM ESCALATION ALERT{RESET}"
                  f"{'':>34}{RED}║{RESET}")
            print(f"  {RED}╠{'═'*56}╣{RESET}")
            for line in p["escalate_msg"].split("\n"):
                pad = 56 - len(line) - 2
                print(f"  {RED}║{RESET}  {line}{' '*max(0,pad)}{RED}║{RESET}")
            print(f"  {RED}╚{'═'*56}╝{RESET}")
        else:
            print(f"  {YELLOW}→ {p['escalate_msg']}{RESET}")

        print()
        time.sleep(1.0)

    # ── Summary Table ─────────────────────────────────────────────────────────
    hr("ACQUISITION FUNNEL SUMMARY", CYAN)

    print(f"  {CYAN}{'─'*66}{RESET}")
    print(f"  {BOLD}{'NAME':<18} {'SCORE':>5}  {'PRODUCT':<18} "
          f"{'CHANNEL':<10} {'ACTION':<22} {'RBI'}{RESET}")
    print(f"  {CYAN}{'─'*66}{RESET}")

    for p in PROSPECTS:
        sc = p["score"]
        sc_color = GREEN if sc >= 80 else YELLOW
        action_color = RED if p["escalate"] else YELLOW
        rbi = f"{GREEN}✅{RESET}" if p["compliance"] else f"{RED}❌{RESET}"
        action_short = "ESCALATE TO RM" if p["escalate"] else "FOLLOW-UP"

        print(f"  {p['name']:<18} "
              f"{sc_color}{BOLD}{sc:>5}{RESET}  "
              f"{p['product']:<18} "
              f"{p['channel']:<10} "
              f"{action_color}{action_short:<22}{RESET} "
              f"{rbi}")

    print(f"  {CYAN}{'─'*66}{RESET}\n")

    escalated = sum(1 for p in PROSPECTS if p["escalate"])
    compliant  = sum(1 for p in PROSPECTS if p["compliance"])

    print(f"  {BOLD}Total Prospects Processed:{RESET}  {len(PROSPECTS)}")
    print(f"  {BOLD}Outreach Messages Sent:{RESET}     {GREEN}{compliant} (RBI-compliant){RESET}")
    print(f"  {BOLD}RM Escalations Triggered:{RESET}   {RED}{escalated} hot leads{RESET}")
    print(f"  {BOLD}Compliance Pass Rate:{RESET}        "
          f"{GREEN}{int(compliant/len(PROSPECTS)*100)}%{RESET}\n")

    print(f"{CYAN}{'═'*70}{RESET}")
    print(f"  {BOLD}{WHITE}AcquireIQ Pipeline Complete{RESET}")
    print(f"  {DIM}Every Indian deserves to be found by their bank.{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}\n")

if __name__ == "__main__":
    main()
