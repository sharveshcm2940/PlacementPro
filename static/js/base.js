// ─── PlacePrep Base JS ───────────────────────────────────────────────────────

// Live date
const dateEl = document.getElementById('live-date');
if (dateEl) {
  const updateDate = () => {
    dateEl.textContent = new Date().toLocaleDateString('en-IN', {
      weekday: 'short', day: 'numeric', month: 'short', year: 'numeric'
    });
  };
  updateDate();
}

// Toast
function showToast(msg, type = '') {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.className = 'toast show ' + (type || '');
  setTimeout(() => t.className = 'toast', 3000);
}

// Sidebar toggle
function toggleSidebar() {
  document.getElementById('sidebar')?.classList.toggle('open');
}

// Logout
async function logout() {
  await fetch('/api/logout', { method: 'POST' });
  window.location.href = '/';
}

// Load notification badge
async function loadNotifBadge() {
  try {
    const res = await fetch('/api/notifications');
    if (!res.ok) return;
    const data = await res.json();
    const badge = document.getElementById('notif-badge');
    if (badge && data.unread > 0) {
      badge.style.display = 'grid';
      badge.textContent = data.unread;
    }
  } catch (e) {}
}

// Load badge on every protected page
if (document.getElementById('sidebar')) {
  loadNotifBadge();
}

// Close sidebar on outside click (mobile)
document.addEventListener('click', e => {
  const sidebar = document.getElementById('sidebar');
  if (!sidebar) return;
  if (sidebar.classList.contains('open') &&
      !sidebar.contains(e.target) &&
      !e.target.closest('.sidebar-toggle')) {
    sidebar.classList.remove('open');
  }
});
