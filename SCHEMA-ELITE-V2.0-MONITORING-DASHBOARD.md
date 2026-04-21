# Schema Elite v2.0 — 30-Day Monitoring Dashboard
**Deployment Date:** 2026-04-21  
**Monitoring Period:** 2026-04-21 to 2026-05-21

---

## Daily Checklist (First 7 Days)

### Day 1-2 (2026-04-21 to 2026-04-22)
**Goal:** Verify no new crawl errors introduced

| Task | Status | Notes |
|------|--------|-------|
| Schema injected to all 44 LPs | ✓ | 120/120 files uploaded to R2 |
| Goiânia LP tested with Google Rich Results | Pending | https://search.google.com/test/rich-results |
| Check console errors (Dev Tools) | Pending | Inspect all 4 rich result types detected |
| GSC: Request indexing (5 LPs) | Pending | goiania-go/*, brasilia-df/aluguel-de-empilhadeira-combustao only |
| GSC: Coverage report (no new errors) | Pending | Should stay green |

### Day 3-7 (2026-04-23 to 2026-04-27)
**Goal:** Detect first rich results impressions

| Metric | Tool | Baseline | D+3 Target | How to Find |
|--------|------|----------|-----------|------------|
| **Rich Results Impressions** | GSC | 100% (baseline measure D+1) | +50% visible | Reports > Performance > Filter by "Page" |
| **FAQ Impressions** | GSC | 0% | 5-10% LPs seeing FAQ impressions | Reports > by Rich Result Type |
| **HowTo Impressions** | GSC | 0% | 2-5% LPs | Same report |
| **VideoObject Impressions** | GSC | Current baseline | +50% from baseline | Same report |
| **Crawl Errors** | GSC | 0 | 0 (no new) | Coverage tab |

---

## Weekly Metrics (Weeks 1-4)

### Week 1 (2026-04-21 to 2026-04-27)
| Metric | Source | Target | Status |
|--------|--------|--------|--------|
| Schema fully indexed | GSC | All 44 LPs indexed | Pending |
| Rich impressions cumulative | GSC | +100-150% from baseline | Pending |
| Featured snippet CTR | GSC | 2-3% (watch for increase) | Pending |
| Position change | GSC | Stable or improving | Pending |
| WhatsApp clicks | GA4 | Baseline established | Pending |
| Organic sessions | GA4 | Stable | Pending |

### Week 2 (2026-04-28 to 2026-05-04)
| Metric | Target | Status |
|--------|--------|--------|
| Rich impressions | +150-200% from baseline | TBD |
| FAQ impressions visible | 20-30% of 44 LPs | TBD |
| Featured snippet appearances | 3-5 positions | TBD |
| Position improvement | -1 to -2 spots | TBD |
| WhatsApp CTR | +100-150% from baseline | TBD |

### Week 3-4 (2026-05-05 to 2026-05-19)
| Metric | Target | Status |
|--------|--------|--------|
| Rich impressions | Stabilize at +150%+ | TBD |
| Featured snippet CTR | +45-55% | TBD |
| Organic traffic | +20-30% visible | TBD |
| Position | -2 to -3 spots | TBD |

---

## Day 30 Full Report (2026-05-21)

### Expected Results by May 21

| Metric | Baseline | Expected | Actual | Variance |
|--------|----------|----------|--------|----------|
| **Rich Results Impressions** | 100% | +150% (250%) | TBD | TBD |
| **FAQ Impressions** | 0% | 50-70% LPs | TBD | TBD |
| **Video Carousel** | Current | +200% | TBD | TBD |
| **Featured Snippet CTR** | 2-3% | +45-55% (3-4.5%) | TBD | TBD |
| **WhatsApp Clicks** | 100% | +250% | TBD | TBD |
| **Organic Traffic (30d)** | 100% | +50-70% | TBD | TBD |
| **Avg Position** | Current | -2 to -5 spots | TBD | TBD |

---

## Google Search Console Submission Checklist

### Phase 1: Request Indexing (Today, 2026-04-21 after 2PM)
1. Open Google Search Console → movemaquinas.com.br
2. Go to: URL Inspection tool
3. Submit for indexing (one-click) for:
   - https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao/
   - https://movemaquinas.com.br/brasilia-df/aluguel-de-empilhadeira-combustao/
   - https://movemaquinas.com.br/anapolis-go/aluguel-de-empilhadeira-combustao/

**Expected Timeline:** 24-48 hours for Google to crawl and detect schema

### Phase 2: Monitor Structured Data Report (D+2, 2026-04-23)
1. GSC → Coverage tab
2. Look for: "Structured data" subsection
3. Verify all 4 rich result types detected:
   - FAQPage
   - HowTo
   - VideoObject
   - Product

**Expected Status:** No errors, 0-3 warnings acceptable

### Phase 3: Verify Rich Results Report (D+7, 2026-04-28)
1. GSC → Enhancements menu
2. Click: "Rich results"
3. Expand "Valid items"
4. Expected breakdown:
   - FAQ: 10-20 items
   - HowTo: 5-10 items
   - VideoObject: 6-8 items
   - Product: 30-40 items

---

## GA4 Tracking Setup

### Event to Monitor: WhatsApp Clicks
**Filter:** External Link Click events with `wa.me` parameter

```
Events > external_link_click
Filter: link_url contains "wa.me"
Time Range: D+0 to D+30
Baseline: Measure this first 2 hours after upload
```

**Expected:** +250% increase by D+14

### Report: Organic Traffic Growth
**View:** Acquisition > Organic Traffic

```
Date Range: D+0 to D+30 vs. Previous 30 days (baseline)
Segments: organic sessions, conversion rate
Expected: +50-70% lift by D+30
```

---

## Daily Log Template

Use this template to track daily observations:

```
Date: YYYY-MM-DD
Time Checked: HH:MM BRT

GSC Observations:
- Rich impressions: [number or % change]
- New errors: [yes/no, list if any]
- URL indexing status: [indexed/pending/excluded]

GA4 Observations:
- WhatsApp clicks: [number]
- Organic sessions: [number]
- Avg position (for top 10 queries): [positions]

Notes:
[Any issues or observations]

Action Items for Next Check:
- [ ] Task 1
- [ ] Task 2
```

---

## Troubleshooting During Monitoring

### "Rich results still not showing (D+3)"
**Status:** Normal. Google takes 24-48 hours minimum.
**Action:** Request indexing via GSC URL Inspection (Fetch as Google)

### "Crawl errors increased"
**Status:** Check what types of errors.
**Action:** 
1. GSC > Coverage > Click error type
2. Identify affected LPs
3. If schema-related: Validate at https://schema.org/Validator
4. If HTML-related: Check that old schema was properly removed

### "Position dropped instead of improved (D+7)"
**Status:** Possible adjustment phase. Schema takes 10-14 days to fully factor.
**Action:** 
1. Verify no other changes made (no content updates, no robots.txt changes)
2. Check that all 44 LPs have valid schema
3. Resubmit 5 LPs to GSC
4. Wait until D+14 before conclusion

### "WhatsApp clicks not increasing"
**Status:** Possible GA4 tracking misconfiguration.
**Action:**
1. Verify ga.js is still loaded (Inspect > Console)
2. Click WhatsApp link and check GA4 real-time report
3. If event fires: tracking is working, wait for data accumulation
4. If event doesn't fire: check that wa.me link is still in schema

---

## Success Gates by Phase

### Phase 1 Gate: First 48 Hours (2026-04-21 to 2026-04-23)
**Must have:**
- ✓ 0 new crawl errors in GSC
- ✓ Schema detected on at least 5 sample LPs
- ✓ No JavaScript console errors

**Decision:** Proceed to Phase 2 (13-city hub)

### Phase 2 Gate: First 7 Days (2026-04-21 to 2026-04-27)
**Must have:**
- ✓ +100% rich impressions beginning to appear (or 20%+ of LPs showing FAQ)
- ✓ 0 new schema validation errors
- ✓ Organic traffic stable or increasing

**Decision:** Proceed to Phase 3 (remaining 21 LPs after content creation)

### Phase 3 Gate: Day 14-21 (2026-05-05 to 2026-05-12)
**Must have:**
- ✓ +150% rich impressions confirmed in GSC
- ✓ Featured snippet appearances visible (3-5 queries)
- ✓ Position improvement (-2 to -5 spots) for key queries

**Decision:** Full success criteria met. Maintain 30-day monitoring.

---

## Monthly Report Template (Due 2026-05-21)

**Title:** Schema Elite v2.0 — 30-Day Impact Report

**Section 1: Executive Summary**
- Total impressions gained: X
- Total clicks gained: Y
- Total traffic uplift: Z%
- Key findings: [3-5 bullets]

**Section 2: Metrics Achieved**
- Rich impressions: Baseline X → Current Y (+Z%)
- Featured snippet: Baseline X queries → Current Y queries (+Z%)
- Position: Baseline AVG X → Current AVG Y (-Z spots)
- Organic traffic: Baseline X sessions → Current Y sessions (+Z%)

**Section 3: By Rich Result Type**
- FAQ: X impressions, Y CTR
- HowTo: X impressions, Y CTR
- VideoObject: X impressions, Y CTR
- Product: X impressions, Y CTR

**Section 4: Issues Encountered**
- [None] / [List issues, resolutions, timeline]

**Section 5: Recommendations**
- Continue with Phase 3 (remaining 21 LPs)
- [Additional recommendations based on results]

---

**Status:** MONITORING IN PROGRESS  
**Last Updated:** 2026-04-21 02:45 BRT  
**Next Review:** 2026-04-22 18:00 BRT
