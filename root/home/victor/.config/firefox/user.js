// =========================
// --- Wayland & Scaling ---
// =========================
user_pref("widget.wayland.fractional-scale.enabled", true);
user_pref("MOZ_ENABLE_WAYLAND", true); // set in environment if needed
user_pref("MOZ_X11_EGL", true); // set in environment if needed

// =========================
// --- Web Rendering & GPU ---
// =========================
user_pref("gfx.webrender.all", true);              // full GPU pipeline
user_pref("gfx.webrender.compositor", true);       // let compositor handle vsync
user_pref("layers.acceleration.force-enabled", true);
user_pref("media.ffmpeg.vaapi.enabled", true);     // hardware video decode

// =========================
// --- Scrolling & Input ---
// =========================
user_pref("general.smoothScroll", true);
user_pref("mousewheel.min_line_scroll_amount", 25);
user_pref("layout.frame_rate", 0);                 // auto monitor refresh
user_pref("dom.event.default_to_passive", true);   // faster event handling

// =========================
// --- Background / CPU ---
// =========================
user_pref("dom.min_background_timeout_value", 1000);  // reduce idle CPU
user_pref("network.prefetch-next", false);
user_pref("network.dns.disablePrefetch", true);
user_pref("network.predictor.enabled", false);
user_pref("image.mem.decode_bytes_at_a_time", 65536);

// =========================
// --- Telemetry & Privacy ---
// =========================
user_pref("toolkit.telemetry.enabled", false);
user_pref("toolkit.telemetry.unified", false);
user_pref("datareporting.healthreport.uploadEnabled", false);
user_pref("network.lna.block_trackers", true);
user_pref("network.lna.blocking", true);

// =========================
// --- Startup & Session ---
// =========================
user_pref("browser.sessionstore.interval", 60000);   // fewer disk writes
user_pref("browser.compactmode.show", true);         // optional UI tweak
