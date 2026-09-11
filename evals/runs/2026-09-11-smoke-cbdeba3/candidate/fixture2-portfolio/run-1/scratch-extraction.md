# Step 1 scope
Teams (5, from file headings): Dispatch, Courier, Core Systems, Insights, Accounts -> PORTFOLIO MODE
Period: Q1 2027. Source: sample-portfolio-2.md (local). Strategy source: "Company Q1 2027 priorities" C1-C4 (lines 10-13).

# Step 2 normalized inventories (verbatim, line-anchored)
Dispatch (L17-31, owner Mei L.; L19 "Commitment: KRs are committed unless marked (stretch).")
 DS1 L21 "Delight enterprise dispatchers and expand Coppervale into two new regions" (supports C1)
  DS1.1 L22 NPS 24->40 Delighted "Dispatcher NPS"
  DS1.2 L23 pilots DE/FR 0->6 CRM "Intl Pilots"
 DS2 L25 "Enterprise teams run their whole day in Coppervale dispatch" (supports C1)
  DS2.1 L26 on-time delivery rate, completed jobs denom, weekly, Ops Console, 91->95
  DS2.2 L27 600 enterprise trial starts via partner portal launch 0->600  [dep: Accounts portal]
  DS2.3 L28 route plan median 14->6 min
  DS2.4 L29 "Reduce the failure rate from 6% to 3%" -> AP-13 ambiguous denominator
 Notes L31: DS2.2 assumes partner portal; Accounts owns portal build.

Courier (L35-49, owner Tomas R.; NO commitment convention line) -> AP-08 set-level
 CR1 L38; CR1.1 L39 crash-free 99.2->99.6; CR1.2 L40 retention 71->78 (matches appendix 71)
 CR2 L42; CR2.1 L43 referral installs 3,000->45,000 (15x, no mechanism) -> AP-07; single KR -> K6=0
 CR3 L45; CR3.1 L46 0/14->14/14 (baseline->target: AP-01 EXCLUDED); dep on Core Systems SDK GA
         CR3.2 L47 event loss rate, denom defined (non-defect)
 Notes L49 "referral growth is our big swing this quarter"; "SDK timing per Core Systems' plan."

Core Systems (L53-70, owner Adaeze O., committed-unless-stretch L55)
 CS1 L57 "Continue running the platform smoothly for every team" -> AP-10 path (a)
  CS1.1 L58 Sev-1 9->=<4 (baseline matches appendix L120 -> non-defect); CS1.2 L59 $0.42->$0.30 (= C4)
 CS2 L61 "Ship with confidence" (supports C2 - enterprise churn) -> AL-05 cascade drift
  CS2.1 deploy freq 2->8/wk; CS2.2 CFR 18->8%; CS2.3 CI p95 42->15min
 CS3 L66; CS3.1 L67 SDK GA after Insights validates v3, internal apps 1->3 (AP-01 EXCLUDED); CS3.2 L68 45s->12s
 Notes L70 "GA is gated on schema v3 validation (Insights)."

Insights (L74-87, owner Halima D., committed-unless-stretch + "Owners listed per KR" L76)
 IN1 L78 exec dashboards (supports C4); IN1.1 L79 14->35; IN1.2 L80 9s->3s; IN1.3 L81 App Store rating 4.1->4.6 -> AP-12 orphan
 IN2 L83; IN2.1 L84 0/22->22/22 after Courier instruments (dep); IN2.2 L85 2/9->9/9 "Owner: TBD." -> AP-15
 Notes L87 "schema v3 validation is sequenced behind Courier's instrumentation"

Accounts (L91-111, owner Georg B., committed-unless-stretch L93)
 AC1/AC2/AC3/AC4 all "(Priority: P0)" + L111 "every one of these is P0" -> AP-05
 AC1.1 L96 TTV 19->7d; AC1.2 L97 54->80% denom stated (non-defect)
 AC2.1 L100 backlog 210->60; AC2.2 L101 CSAT 86->90 "Q4 2026 baseline" vs appendix L118 CSAT 78 -> AL-09
 AC3.1 L104 on-time delivery rate, scheduled-incl-cancellations denom, monthly, Billing warehouse, 78->85 -> AL-08 vs DS2.1
 AC3.2 L105 partner portal 0->40 "(stretch - only if the billing migration lands early)" -> AL-12 vs DS2.2
 AC4.1 L108 4.2->1.5%; AC4.2 L109 migration 38->100% of 6,400 accounts (AP-01 EXCLUDED)

# Step 4 structures
Dependency edges: Courier CR3.1 -> Core Systems (SDK GA); Core Systems CS3.1 -> Insights (schema v3);
 Insights IN2.1 -> Courier (instrumentation)  => CYCLE (AL-11, Critical)
 Dispatch DS2.2 -> Accounts (portal, acknowledged both sides but commitment mismatch => AL-12, not AL-01)
Metric catalog collisions: "On-time delivery rate" x2 (AL-08); "Customer CSAT" team vs company review (AL-09)
Strategy trace: C1 <- DS1,DS2,AC4; C2 <- AC1,AC2,AC3,(CS2 = drift); C3 <- CR1,CR2; C4 <- CS1,CS3,CR3,IN1,IN2. No uncovered pillar -> no AL-10.
Disconfirmed/killed: AL-01 on portal (Accounts acknowledges); AL-05 on CR3->C4 (C4 names telemetry consolidation);
 AL-09 on on-time delivery (definition split -> reported as AL-08); AL-07 (no capacity statement, no multi-claimant node);
 AP-01 on CR3.1/CS3.1/AC4.2 (baseline->target exclusion); AP-13 on CR3.2/AC1.2/AC4.1/CS2.2 (denominators stated).
