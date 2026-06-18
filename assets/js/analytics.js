/* =====================================================================
   ABI — Analytics & Ads (GA4 · Google Ads · Meta Pixel)
   HOW TO ACTIVATE: paste your IDs below. Until then nothing loads
   (no errors, no tracking). Conversion events fire automatically on
   form submits and phone-call clicks once IDs are set.
   ===================================================================== */
(function () {
  "use strict";
  var CFG = {
    GA4_ID:        "",   // e.g. "G-XXXXXXXXXX"  (Google Analytics 4)
    GOOGLE_ADS_ID: "",   // e.g. "AW-XXXXXXXXXX" (Google Ads)
    GADS_LEAD_LABEL: "", // e.g. "abcDEFghIJ"     (Ads conversion label for a lead)
    META_PIXEL_ID: ""    // e.g. "1234567890"     (Meta / Facebook Pixel)
  };
  window.ABI_ANALYTICS = CFG;

  // ---- Google Analytics 4 + Google Ads (gtag) ----
  if (CFG.GA4_ID || CFG.GOOGLE_ADS_ID) {
    var id = CFG.GA4_ID || CFG.GOOGLE_ADS_ID;
    var s = document.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag("js", new Date());
    if (CFG.GA4_ID) gtag("config", CFG.GA4_ID);
    if (CFG.GOOGLE_ADS_ID) gtag("config", CFG.GOOGLE_ADS_ID);
  }

  // ---- Meta (Facebook) Pixel ----
  if (CFG.META_PIXEL_ID) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
      (window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", CFG.META_PIXEL_ID); fbq("track", "PageView");
  }

  // ---- Unified event helper used by abi.js ----
  window.abiTrack = function (name, params) {
    params = params || {};
    try { if (window.gtag) gtag("event", name, params); } catch (e) {}
    try {
      if (window.fbq) {
        var map = { generate_lead: "Lead", contact: "Contact", begin_checkout: "InitiateCheckout" };
        fbq("track", map[name] || "CustomEvent", params);
      }
    } catch (e) {}
    // Google Ads conversion on lead
    try {
      if (name === "generate_lead" && window.gtag && CFG.GOOGLE_ADS_ID && CFG.GADS_LEAD_LABEL) {
        gtag("event", "conversion", { send_to: CFG.GOOGLE_ADS_ID + "/" + CFG.GADS_LEAD_LABEL });
      }
    } catch (e) {}
  };
})();
