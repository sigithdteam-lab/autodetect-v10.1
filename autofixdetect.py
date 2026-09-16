#!/usr/bin/env python3
# GNU General Public License v3.0
# Copyright (C) 2026 sigithdteam-lab

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           AUTOFIXDETECT AI v10.1 - ULTIMATE FINAL EDITION                  ║
║                                                                            ║
║   ⚡ AI-Powered System Diagnostic & Auto-Fix Tool                          ║
║   🧠 Self-Learning with 16-Source Internet Search & Improvisation         ║
║   🌐 Full Web Interface with Real-Time Progress                           ║
║   📚 No External Dependencies - Fully Self-Contained                      ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import platform
import subprocess
import json
import time
import shutil
import socket
import re
import threading
import uuid
import urllib.request
import urllib.parse
import ssl
import hashlib
import signal
import tempfile
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Optional, Any, Set, Tuple
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

#===============================================================================
# VERSION INFORMATION
#===============================================================================
VERSION = "10.1"
VERSION_NAME = "Ultimate Final Edition"
RELEASE_DATE = "2026-09-16"

#===============================================================================
# COLOR SYSTEM
#===============================================================================
class Colors:
    """Advanced color system with fallback for non-terminal environments"""
    def __init__(self):
        self.use_colors = sys.stdout.isatty() and os.environ.get('TERM') != 'dumb'
        if self.use_colors:
            self.RED = '\033[0;31m'
            self.GREEN = '\033[0;32m'
            self.YELLOW = '\033[1;33m'
            self.BLUE = '\033[0;34m'
            self.CYAN = '\033[0;36m'
            self.WHITE = '\033[1;37m'
            self.BOLD = '\033[1m'
            self.DIM = '\033[2m'
            self.NC = '\033[0m'
            self.PURPLE = '\033[0;35m'
            self.ORANGE = '\033[38;5;208m'
            self.PINK = '\033[38;5;205m'
            self.UNDERLINE = '\033[4m'
            self.BLINK = '\033[5m'
            self.REVERSE = '\033[7m'
        else:
            self.RED = self.GREEN = self.YELLOW = self.BLUE = ''
            self.CYAN = self.WHITE = self.BOLD = self.DIM = self.NC = ''
            self.PURPLE = self.ORANGE = self.PINK = self.UNDERLINE = ''
            self.BLINK = self.REVERSE = ''

colors = Colors()

#===============================================================================
# EMBEDDED WEB UI
#===============================================================================
WEB_UI_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AutoFixDetect AI v10.1 - Ultimate</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --bg-primary: #0a0a1a;
            --bg-secondary: #12122a;
            --bg-card: rgba(255,255,255,0.03);
            --border-color: rgba(255,255,255,0.06);
            --text-primary: #ffffff;
            --text-secondary: rgba(255,255,255,0.6);
            --accent-1: #00d2ff;
            --accent-2: #3a7bd5;
            --accent-3: #7c3aed;
            --success: #4ade80;
            --warning: #fbbf24;
            --danger: #f87171;
            --info: #60a5fa;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 20px;
            background-image: 
                radial-gradient(ellipse at 10% 20%, rgba(0,210,255,0.05) 0%, transparent 50%),
                radial-gradient(ellipse at 90% 80%, rgba(124,58,237,0.05) 0%, transparent 50%);
        }
        .container { max-width: 1300px; margin: 0 auto; }
        .header {
            text-align: center;
            padding: 25px 0 30px;
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }
        .header .version-badge {
            display: inline-block;
            padding: 4px 16px;
            border-radius: 20px;
            font-size: 0.7em;
            font-weight: 600;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-3));
            color: #fff;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }
        .header h1 {
            font-size: 2.8em;
            font-weight: 800;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-2), var(--accent-3));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .header .subtitle {
            color: var(--text-secondary);
            margin-top: 8px;
            font-size: 1.1em;
        }
        .header .features {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 15px;
            font-size: 0.85em;
            color: var(--text-secondary);
        }
        .header .features span {
            padding: 4px 12px;
            border-radius: 12px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
        }
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 15px;
            margin: 25px 0;
        }
        .card {
            background: var(--bg-card);
            backdrop-filter: blur(10px);
            padding: 18px 15px;
            border-radius: 14px;
            border: 1px solid var(--border-color);
            text-align: center;
            transition: all 0.3s ease;
        }
        .card:hover { transform: translateY(-3px); border-color: rgba(255,255,255,0.1); }
        .card .icon { font-size: 1.5em; margin-bottom: 5px; }
        .card h3 { font-size: 0.65em; opacity: 0.5; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
        .card .value { font-size: 2.2em; font-weight: 700; }
        .card .sub { font-size: 0.7em; opacity: 0.5; margin-top: 4px; }
        .card.green .value { color: var(--success); }
        .card.yellow .value { color: var(--warning); }
        .card.red .value { color: var(--danger); }
        .card.blue .value { color: var(--info); }
        .card.purple .value { color: var(--accent-3); }
        .card.cyan .value { color: var(--accent-1); }
        .progress-section {
            background: var(--bg-card);
            border-radius: 14px;
            padding: 20px;
            margin: 15px 0;
            border: 1px solid var(--border-color);
            display: none;
        }
        .progress-section.active { display: block; }
        .progress-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        .progress-title { font-weight: 600; font-size: 0.95em; }
        .progress-title .highlight { color: var(--accent-1); }
        .progress-percent { font-size: 1.4em; font-weight: 700; color: var(--accent-1); }
        .progress-track {
            width: 100%;
            height: 10px;
            background: rgba(255,255,255,0.06);
            border-radius: 6px;
            overflow: hidden;
        }
        .progress-track .fill {
            height: 100%;
            border-radius: 6px;
            transition: width 0.4s ease;
            width: 0%;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-3));
        }
        .progress-track .fill.complete { background: linear-gradient(45deg, var(--success), #16a34a); }
        .progress-status {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-size: 0.85em;
            color: var(--text-secondary);
        }
        .progress-details {
            margin-top: 15px;
            padding: 12px;
            background: rgba(0,0,0,0.3);
            border-radius: 10px;
            max-height: 180px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.8em;
            line-height: 1.6;
        }
        .progress-details::-webkit-scrollbar { width: 4px; }
        .progress-details::-webkit-scrollbar-track { background: rgba(255,255,255,0.03); border-radius: 2px; }
        .progress-details::-webkit-scrollbar-thumb { background: var(--accent-2); border-radius: 2px; }
        .detail-item { padding: 3px 0; border-bottom: 1px solid rgba(255,255,255,0.02); }
        .detail-item.success { color: var(--success); }
        .detail-item.error { color: var(--danger); }
        .detail-item.info { color: var(--info); }
        .detail-item.warn { color: var(--warning); }
        .detail-item.ai { color: var(--accent-3); }
        .btn-group {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px 0;
        }
        .btn {
            padding: 10px 28px;
            border: none;
            border-radius: 25px;
            font-size: 0.95em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #fff;
            position: relative;
            overflow: hidden;
        }
        .btn-primary { background: linear-gradient(45deg, var(--accent-1), var(--accent-2)); }
        .btn-success { background: linear-gradient(45deg, var(--success), #16a34a); }
        .btn-danger { background: linear-gradient(45deg, var(--danger), #dc2626); }
        .btn-warning { background: linear-gradient(45deg, var(--warning), #f59e0b); color: #000; }
        .btn-purple { background: linear-gradient(45deg, var(--accent-3), #6d28d9); }
        .btn:hover { transform: scale(1.04); box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        .btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }
        .status-section {
            background: var(--bg-card);
            border-radius: 14px;
            padding: 18px 20px;
            margin: 15px 0;
            border: 1px solid var(--border-color);
        }
        .status-section h3 {
            font-size: 0.85em;
            opacity: 0.6;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.03);
        }
        .status-item:last-child { border-bottom: none; }
        .status-badge {
            padding: 3px 14px;
            border-radius: 15px;
            font-size: 0.65em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .status-badge.ok { background: rgba(74,222,128,0.15); color: var(--success); }
        .status-badge.warn { background: rgba(251,191,36,0.15); color: var(--warning); }
        .status-badge.error { background: rgba(248,113,113,0.15); color: var(--danger); }
        .status-badge.running { background: rgba(96,165,250,0.15); color: var(--info); animation: pulse 1.2s infinite; }
        .status-badge.ai { background: rgba(124,58,237,0.15); color: var(--accent-3); }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .error-summary {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            padding: 12px 16px;
            background: rgba(0,0,0,0.2);
            border-radius: 10px;
            margin-top: 10px;
        }
        .error-summary .item { font-size: 0.85em; }
        .error-summary .count { font-weight: 700; }
        .error-summary .count.critical { color: var(--danger); }
        .error-summary .count.warning { color: var(--warning); }
        .error-summary .count.info { color: var(--info); }
        .logs {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 15px;
            max-height: 180px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.78em;
            line-height: 1.5;
            margin-top: 10px;
        }
        .logs::-webkit-scrollbar { width: 4px; }
        .logs::-webkit-scrollbar-track { background: rgba(255,255,255,0.03); border-radius: 2px; }
        .logs::-webkit-scrollbar-thumb { background: var(--accent-2); border-radius: 2px; }
        .log-entry { padding: 2px 0; border-bottom: 1px solid rgba(255,255,255,0.02); }
        .log-entry .time { color: var(--text-secondary); opacity: 0.5; }
        .log-entry.info { color: var(--success); }
        .log-entry.warn { color: var(--warning); }
        .log-entry.error { color: var(--danger); }
        .log-entry.ai { color: var(--accent-3); }
        .log-entry.progress { color: var(--info); }
        @media (max-width: 768px) {
            .header h1 { font-size: 2em; }
            .dashboard { grid-template-columns: repeat(3, 1fr); gap: 10px; }
            .card { padding: 12px 10px; }
            .card .value { font-size: 1.6em; }
            .btn-group { flex-direction: column; }
            .btn { width: 100%; }
            .header .features { font-size: 0.7em; gap: 8px; }
        }
        @media (max-width: 480px) {
            .dashboard { grid-template-columns: repeat(2, 1fr); }
            .header h1 { font-size: 1.5em; }
            body { padding: 10px; }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="version-badge">⚡ v10.1 ULTIMATE</div>
        <h1>🛠 AutoFixDetect AI</h1>
        <div class="subtitle">AI-Powered Self-Learning System Diagnostic & Auto-Fix</div>
        <div class="features">
            <span>🧠 AI Improvisation</span>
            <span>🌐 16-Source Search</span>
            <span>📚 Self-Learning</span>
            <span>⚡ Real-Time Progress</span>
        </div>
        <div class="btn-group">
            <button class="btn btn-primary" onclick="runDiagnostic()" id="runBtn">🔍 Scan System</button>
            <button class="btn btn-success" onclick="runFix()" id="fixBtn" disabled>🧠 AI Fix All</button>
            <button class="btn btn-warning" onclick="runFixFast()" id="fastBtn" disabled>⚡ Fast Fix</button>
            <button class="btn btn-danger" onclick="stopFix()" id="stopBtn" disabled>⏹ Stop</button>
            <button class="btn btn-purple" onclick="clearLogs()">🗑 Clear Logs</button>
        </div>
    </div>

    <div class="dashboard" id="dashboard">
        <div class="card green"><div class="icon">❤️</div><h3>Health</h3><div class="value" id="healthScore">100</div><div class="sub">/100</div></div>
        <div class="card red"><div class="icon">🔴</div><h3>Critical</h3><div class="value" id="criticalErrors">0</div><div class="sub">errors</div></div>
        <div class="card yellow"><div class="icon">🟡</div><h3>Warnings</h3><div class="value" id="warnings">0</div><div class="sub">issues</div></div>
        <div class="card blue"><div class="icon">🔧</div><h3>Fixes</h3><div class="value" id="fixesApplied">0</div><div class="sub">applied</div></div>
        <div class="card purple"><div class="icon">🧠</div><h3>AI Progress</h3><div class="value" id="progressCount">0%</div><div class="sub" id="progressSub">idle</div></div>
        <div class="card cyan"><div class="icon">📊</div><h3>Errors</h3><div class="value" id="totalErrors">0</div><div class="sub">total detected</div></div>
    </div>

    <div class="progress-section" id="progressSection">
        <div class="progress-header">
            <span class="progress-title">🧠 <span class="highlight" id="progressTitle">AI Improvising...</span></span>
            <span class="progress-percent" id="progressPercent">0%</span>
        </div>
        <div class="progress-track"><div class="fill" id="progressBar"></div></div>
        <div class="progress-status">
            <span id="progressStatus">Initializing AI engine...</span>
            <span id="progressCountLabel">0 / 0</span>
        </div>
        <div class="progress-details" id="progressDetails">
            <div class="detail-item info">⏳ AI Engine ready. Waiting for commands...</div>
        </div>
    </div>

    <div class="status-section">
        <h3>📊 Error Summary</h3>
        <div class="error-summary" id="errorSummary">
            <div class="item">🔴 SYSTEMD_FAILURE: <span class="count critical" id="systemdCount">0</span></div>
            <div class="item">🟡 Other Errors: <span class="count warning" id="otherCount">0</span></div>
            <div class="item">📌 Unique Errors: <span class="count info" id="uniqueCount">0</span></div>
            <div class="item">🧠 AI Solutions: <span class="count info" id="aiSolutions">0</span></div>
        </div>
    </div>

    <div class="status-section">
        <h3>📡 System Status</h3>
        <div id="statusList">
            <div class="status-item">
                <span>🟢 AI Engine Active & Ready</span>
                <span class="status-badge ai">AI Ready</span>
            </div>
        </div>
    </div>

    <div class="status-section">
        <h3>📋 Live Logs</h3>
        <div class="logs" id="logs">
            <div class="log-entry ai"><span class="time">[INIT]</span> 🧠 AI Engine initialized. Self-learning mode active.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> 🌐 16-source search engine ready.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> 📚 Learning database loaded.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> ✅ System ready. Click "Scan System" to start.</div>
        </div>
    </div>
</div>

<script>
let isRunning = false;
let isFixing = false;
let eventSource = null;
let fixThreadId = null;

function addLog(message, type = 'info') {
    const logs = document.getElementById('logs');
    const entry = document.createElement('div');
    entry.className = `log-entry ${type}`;
    const time = new Date().toLocaleTimeString();
    entry.innerHTML = `<span class="time">[${time}]</span> ${message}`;
    logs.appendChild(entry);
    logs.scrollTop = logs.scrollHeight;
    while (logs.children.length > 300) logs.removeChild(logs.firstChild);
}

function addDetail(message, type = 'info') {
    const details = document.getElementById('progressDetails');
    const entry = document.createElement('div');
    entry.className = `detail-item ${type}`;
    entry.textContent = message;
    details.appendChild(entry);
    details.scrollTop = details.scrollHeight;
    while (details.children.length > 150) details.removeChild(details.firstChild);
}

function updateDashboard(data) {
    if (!data) return;
    document.getElementById('healthScore').textContent = data.health_score || 100;
    document.getElementById('criticalErrors').textContent = data.critical_errors || 0;
    document.getElementById('warnings').textContent = data.warnings || 0;
    document.getElementById('fixesApplied').textContent = data.fixes_applied || 0;
    document.getElementById('totalErrors').textContent = data.total_errors || 0;
    if (data.error_summary) {
        document.getElementById('systemdCount').textContent = data.error_summary.systemd_count || 0;
        document.getElementById('otherCount').textContent = data.error_summary.other_count || 0;
        document.getElementById('uniqueCount').textContent = data.error_summary.unique_count || 0;
        document.getElementById('aiSolutions').textContent = data.error_summary.ai_solutions || 0;
    }
}

function updateProgress(data) {
    const pct = data.percent || 0;
    document.getElementById('progressPercent').textContent = pct + '%';
    document.getElementById('progressBar').style.width = pct + '%';
    document.getElementById('progressCountLabel').textContent = `${data.current || 0} / ${data.total || 0}`;
    document.getElementById('progressStatus').textContent = data.status || 'Processing...';
    document.getElementById('progressCount').textContent = pct + '%';
    document.getElementById('progressSub').textContent = data.status || 'processing';
    if (data.current_fix) document.getElementById('progressTitle').textContent = data.current_fix;
    if (pct >= 100) {
        document.getElementById('progressBar').className = 'fill complete';
        document.getElementById('progressStatus').textContent = '✅ Complete!';
        document.getElementById('progressSub').textContent = 'complete';
    }
}

function showProgress(show) {
    document.getElementById('progressSection').className = 'progress-section' + (show ? ' active' : '');
}

function updateStatus(statuses) {
    const list = document.getElementById('statusList');
    list.innerHTML = '';
    statuses.forEach(status => {
        const item = document.createElement('div');
        item.className = 'status-item';
        const badge = document.createElement('span');
        badge.className = `status-badge ${status.status}`;
        badge.textContent = status.status.toUpperCase();
        item.innerHTML = `<span>${status.icon || '•'} ${status.message}</span>`;
        item.appendChild(badge);
        list.appendChild(item);
    });
}

async function runDiagnostic() {
    if (isRunning) return;
    isRunning = true;
    document.getElementById('runBtn').disabled = true;
    document.getElementById('fixBtn').disabled = true;
    document.getElementById('fastBtn').disabled = true;
    addLog('🔍 Starting AI-powered system scan...', 'ai');
    try {
        const response = await fetch('/diagnostic', { method: 'POST' });
        const data = await response.json();
        const total = data.summary?.total_errors || 0;
        const systemd = data.error_summary?.systemd_count || 0;
        addLog(`✅ Scan complete: ${total} errors found (${systemd} SYSTEMD errors)`, total > 0 ? 'warn' : 'info');
        updateDashboard(data);
        if (total > 0) {
            document.getElementById('fixBtn').disabled = false;
            document.getElementById('fastBtn').disabled = false;
            addLog(`🧠 AI Engine ready to fix ${total} errors.`, 'ai');
            updateStatus([
                { icon: '🔴', message: `${total} errors detected (${systemd} SYSTEMD)`, status: 'error' },
                { icon: '🧠', message: `AI has ${data.error_summary?.ai_solutions || 0} known solutions`, status: 'ai' }
            ]);
        } else {
            addLog('🎉 No errors detected! System is healthy.', 'info');
            updateStatus([{ icon: '✅', message: 'System is healthy', status: 'ok' }]);
        }
    } catch (error) {
        addLog(`❌ Error: ${error.message}`, 'error');
    }
    isRunning = false;
    document.getElementById('runBtn').disabled = false;
}

async function runFix() { await startFix('full'); }
async function runFixFast() { await startFix('fast'); }

async function startFix(mode) {
    if (isFixing) return;
    isFixing = true;
    document.getElementById('fixBtn').disabled = true;
    document.getElementById('fastBtn').disabled = true;
    document.getElementById('runBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;
    document.getElementById('progressDetails').innerHTML = '';
    showProgress(true);
    addLog(`🧠 AI Engine starting ${mode} fix mode...`, 'ai');
    updateStatus([{ icon: '🧠', message: `AI Fixing (${mode} mode)...`, status: 'running' }]);
    try {
        const response = await fetch('/fix/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mode: mode })
        });
        const data = await response.json();
        fixThreadId = data.thread_id;
        addLog(`📋 Fix session started (ID: ${fixThreadId})`, 'info');
        if (eventSource) eventSource.close();
        eventSource = new EventSource('/fix/progress?thread_id=' + fixThreadId);
        eventSource.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'progress') {
                updateProgress(data);
                if (data.current_fix) addDetail(`🔧 ${data.current_fix}`, 'info');
            } else if (data.type === 'detail') {
                addDetail(`${data.success ? '✅' : '❌'} ${data.message}`, data.success ? 'success' : 'error');
            } else if (data.type === 'ai') {
                addDetail(`🧠 ${data.message}`, 'ai');
            } else if (data.type === 'complete') {
                addLog(`✅ AI Fix complete: ${data.fixes_applied} fixes applied`, 'info');
                if (data.unresolved > 0) addLog(`⚠ ${data.unresolved} errors still need manual intervention`, 'warn');
                updateDashboard(data);
                showProgress(false);
                document.getElementById('fixBtn').disabled = true;
                document.getElementById('fastBtn').disabled = true;
                document.getElementById('stopBtn').disabled = true;
                isFixing = false;
                updateStatus([{ icon: '✅', message: `AI Fixed ${data.fixes_applied} errors`, status: 'ok' }]);
                if (data.unresolved > 0) updateStatus([{ icon: '⚠', message: `${data.unresolved} errors unresolved`, status: 'warn' }]);
                eventSource.close();
                eventSource = null;
            } else if (data.type === 'error') {
                addLog(`❌ Error: ${data.message}`, 'error');
            }
        };
        eventSource.onerror = function() { addLog('⚠ Progress stream disconnected', 'warn'); };
    } catch (error) {
        addLog(`❌ Error: ${error.message}`, 'error');
        isFixing = false;
        document.getElementById('fixBtn').disabled = false;
        document.getElementById('fastBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
        showProgress(false);
    }
}

async function stopFix() {
    if (!isFixing || !fixThreadId) return;
    try {
        const response = await fetch('/fix/stop', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ thread_id: fixThreadId })
        });
        const data = await response.json();
        addLog(`⏹ AI Fix stopped: ${data.message || 'by user'}`, 'warn');
        isFixing = false;
        document.getElementById('fixBtn').disabled = false;
        document.getElementById('fastBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
        showProgress(false);
        if (eventSource) { eventSource.close(); eventSource = null; }
        updateStatus([{ icon: '⏹', message: 'Fix stopped by user', status: 'warn' }]);
    } catch (error) { addLog(`❌ Error: ${error.message}`, 'error'); }
}

function clearLogs() {
    document.getElementById('logs').innerHTML = '';
    addLog('🗑 Logs cleared', 'info');
    document.getElementById('progressDetails').innerHTML = '';
    addDetail('⏳ AI Engine ready.', 'info');
}

setTimeout(() => {
    addLog('🚀 Auto-starting diagnostic scan...', 'ai');
    runDiagnostic();
}, 1500);
</script>
</body>
</html>
'''

#===============================================================================
# AI IMPROVISATION ENGINE v10.1 - 16-SOURCE SEARCH
#===============================================================================
class ImprovisationEngine:
    """AI improvisation engine with multi-source internet search"""

    def __init__(self):
        self.base_dir = '/var/log/autofixdetect'
        self.learning_db = os.path.join(self.base_dir, 'learning_db.json')
        self.search_cache = os.path.join(self.base_dir, 'search_cache.json')
        self.successful_fixes = defaultdict(list)
        self.failed_attempts = defaultdict(list)
        self.error_patterns = self._load_patterns()
        self.ai_solutions_count = 0
        self._ensure_dirs()
        self._load_learning_db()
        self._print_ai_status()

    def _ensure_dirs(self):
        for p in [self.base_dir, os.path.join(self.base_dir, 'solutions')]:
            try:
                os.makedirs(p, exist_ok=True)
            except Exception:
                # fallback ke tmpdir jika /var/log tidak writable
                self.base_dir = tempfile.mkdtemp(prefix='autofixdetect_')
                self.learning_db = os.path.join(self.base_dir, 'learning_db.json')
                self.search_cache = os.path.join(self.base_dir, 'search_cache.json')

    def _print_ai_status(self):
        print(f"{colors.PURPLE}🧠 AI Engine: Active (16-source search){colors.NC}")
        print(f"{colors.DIM}   Learning DB: {len(self.successful_fixes)} patterns learned{colors.NC}")
        print(f"{colors.DIM}   Base dir: {self.base_dir}{colors.NC}")

    # ---------------------------------------------------------------
    # HTTP + HTML helpers
    # ---------------------------------------------------------------
    def _clean_html(self, html: str) -> str:
        """Strip tag HTML & decode entity umum"""
        if not html:
            return ''
        text = re.sub(r'<[^>]+>', ' ', html)
        text = re.sub(r'\s+', ' ', text)
        for ent, ch in [('&quot;', '"'), ('&amp;', '&'), ('&lt;', '<'),
                        ('&gt;', '>'), ('&#39;', "'"), ('&nbsp;', ' '),
                        ('&#x27;', "'"), ('&#x2F;', '/')]:
            text = text.replace(ent, ch)
        return text.strip()

    def _http_get(self, url: str, timeout: int = 8, json_mode: bool = False):
        """HTTP GET dengan SSL verification aktif (fallback ke unverified)."""
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AutoFixDetect/10.1',
            'Accept': 'application/json' if json_mode else 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        try:
            resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        except ssl.SSLError:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        raw = resp.read().decode('utf-8', errors='ignore')
        return json.loads(raw) if json_mode else raw

    # ---------------------------------------------------------------
    # Pattern database
    # ---------------------------------------------------------------
    def _load_patterns(self) -> Dict:
        default_patterns = {
            'systemd_af_vsock': {
                'patterns': [
                    r'Failed to query local AF_VSOCK CID',
                    r'systemd-ssh-generator.*failed',
                    r'AF_VSOCK', r'sd-exec.*failed', r'vsock.*error'
                ],
                'severity': 'critical', 'category': 'systemd',
                'known_fixes': [
                    'systemctl daemon-reload',
                    'systemctl restart systemd-logind',
                    'systemctl restart systemd-udevd',
                    'systemctl restart systemd-journald',
                    'systemctl reset-failed'
                ],
                'search_terms': [
                    'AF_VSOCK CID failed systemd fix',
                    'systemd-ssh-generator AF_VSOCK error debian',
                    'Failed to query local AF_VSOCK CID solution',
                    'systemd vsock error fix'
                ]
            },
            'service_timeout': {
                'patterns': [r'Watchdog timeout', r'service.*timeout',
                             r'Timed out', r'Timeout.*service'],
                'severity': 'warning', 'category': 'systemd',
                'known_fixes': [
                    'systemctl daemon-reload', 'systemctl reset-failed',
                    'systemctl status --failed'
                ],
                'search_terms': [
                    'systemd watchdog timeout fix',
                    'service timeout systemd solution'
                ]
            },
            'service_crashed': {
                'patterns': [r'service.*failed', r'process.*crashed',
                             r'segfault', r'core dumped', r'exited with code'],
                'severity': 'critical', 'category': 'service',
                'known_fixes': [
                    'systemctl reset-failed', 'systemctl daemon-reload',
                    'journalctl -p err -b --no-pager | tail -50'
                ],
                'search_terms': [
                    'service crashed systemd fix',
                    'systemd service failed restart',
                    'process crashed linux fix'
                ]
            },
            'memory_high': {
                'patterns': [r'Out of memory', r'oom-killer',
                             r'Memory usage', r'high memory'],
                'severity': 'warning', 'category': 'memory',
                'known_fixes': [
                    'sync && echo 3 > /proc/sys/vm/drop_caches',
                    'free -h'
                ],
                'search_terms': [
                    'linux high memory usage fix', 'oom killer solution'
                ]
            },
            'disk_full': {
                'patterns': [r'No space left on device', r'disk full',
                             r'ENOSPC', r'not enough free space'],
                'severity': 'critical', 'category': 'disk',
                'known_fixes': [
                    'apt-get clean',
                    'journalctl --vacuum-size=100M',
                    'df -h'
                ],
                'search_terms': [
                    'linux disk full fix', 'no space left on device solution'
                ]
            },
            'network_error': {
                'patterns': [r'connection timed out', r'network.*failed',
                             r'Cannot connect', r'Network is unreachable'],
                'severity': 'warning', 'category': 'network',
                'known_fixes': [
                    'systemctl restart systemd-resolved',
                    'ip -br addr'
                ],
                'search_terms': [
                    'linux network connection timeout fix',
                    'network unreachable solution'
                ]
            },
            'package_error': {
                'patterns': [r'broken package', r'unmet dependencies',
                             r'dpkg.*error', r'package.*failed'],
                'severity': 'critical', 'category': 'package',
                'known_fixes': [
                    'apt-get install -f -y',
                    'dpkg --configure -a'
                ],
                'search_terms': [
                    'apt broken package fix', 'unmet dependencies solution'
                ]
            }
        }
        pattern_file = os.path.join('/var/log/autofixdetect', 'error_patterns.json')
        try:
            os.makedirs('/var/log/autofixdetect', exist_ok=True)
            if os.path.exists(pattern_file):
                with open(pattern_file, 'r') as f:
                    loaded = json.load(f)
                    default_patterns.update(loaded)
                    return default_patterns
            with open(pattern_file, 'w') as f:
                json.dump(default_patterns, f, indent=2)
        except Exception:
            pass
        return default_patterns

    # ---------------------------------------------------------------
    # Learning DB
    # ---------------------------------------------------------------
    def _load_learning_db(self):
        if os.path.exists(self.learning_db):
            try:
                with open(self.learning_db, 'r') as f:
                    data = json.load(f)
                self.successful_fixes = defaultdict(list, data.get('successful', {}))
                self.failed_attempts = defaultdict(list, data.get('failed', {}))
                self.ai_solutions_count = data.get('ai_solutions_count', 0)
                return
            except Exception:
                pass
        self.successful_fixes = defaultdict(list)
        self.failed_attempts = defaultdict(list)
        self.ai_solutions_count = 0
        self._save_learning_db()

    def _save_learning_db(self):
        try:
            with open(self.learning_db, 'w') as f:
                json.dump({
                    'successful': dict(self.successful_fixes),
                    'failed': dict(self.failed_attempts),
                    'ai_solutions_count': self.ai_solutions_count,
                    'last_updated': datetime.now().isoformat()
                }, f, indent=2)
        except Exception:
            pass

    # ===============================================================
    # SEARCH ENGINES — 16 SUMBER FALLBACK
    # ===============================================================
    def search_internet(self, query: str) -> List[Dict]:
        """Cari solusi dari banyak sumber; stop saat command valid ketemu."""
        cache_key = hashlib.md5(query.encode()).hexdigest()
        cache = {}
        if os.path.exists(self.search_cache):
            try:
                with open(self.search_cache, 'r') as f:
                    cache = json.load(f)
                if cache_key in cache:
                    cached = cache[cache_key]
                    if isinstance(cached, list):
                        return cached
            except Exception:
                cache = {}

        print(f"{colors.YELLOW}🔍 Searching: {query[:60]}...{colors.NC}")

        sources = [
            ('Stack Overflow',    self._search_stackoverflow),
            ('Unix SE',           lambda q: self._search_stackexchange(q, 'unix')),
            ('Ask Ubuntu',        lambda q: self._search_stackexchange(q, 'askubuntu')),
            ('Server Fault',      lambda q: self._search_stackexchange(q, 'serverfault')),
            ('Super User',        lambda q: self._search_stackexchange(q, 'superuser')),
            ('GitHub',            self._search_github),
            ('DuckDuckGo',        self._search_duckduckgo),
            ('Google',            self._search_google),
            ('Bing',              self._search_bing),
            ('Reddit',            self._search_reddit),
            ('Arch Wiki',         self._search_arch_wiki),
            ('Searx',             self._search_searx),
            ('Yandex',            self._search_yandex),
            ('Brave',             self._search_brave),
            ('Mojeek',            self._search_mojeek),
            ('Marginalia (deep)', self._search_marginalia),
        ]

        collected: List[Dict] = []
        for name, fn in sources:
            try:
                hits = fn(query) or []
                if not hits:
                    continue
                cmds = self.extract_commands(hits)
                collected.extend(hits)
                if cmds:
                    print(f"{colors.GREEN}   ✅ {name}: {len(cmds)} command{colors.NC}")
                    break
                print(f"{colors.DIM}   ⚠ {name}: tanpa command, lanjut...{colors.NC}")
            except Exception as e:
                print(f"{colors.DIM}   ✗ {name} gagal: {str(e)[:50]}{colors.NC}")
                continue

        if collected:
            try:
                cache[cache_key] = collected
                with open(self.search_cache, 'w') as f:
                    json.dump(cache, f, indent=2)
            except Exception:
                pass
        return collected

    def _search_stackexchange(self, query: str, site: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            url = (f"https://api.stackexchange.com/2.3/search/advanced"
                   f"?order=desc&sort=relevance&q={enc}"
                   f"&site={site}&pagesize=5&filter=withbody")
            data = self._http_get(url, json_mode=True)
            for it in data.get('items', [])[:5]:
                results.append({
                    'source': site,
                    'title': it.get('title', ''),
                    'link': it.get('link', ''),
                    'score': it.get('score', 0),
                    'solution': self._clean_html(it.get('body', ''))[:1500],
                })
        except Exception:
            pass
        return results

    def _search_stackoverflow(self, query: str) -> List[Dict]:
        return self._search_stackexchange(query, 'stackoverflow')

    def _search_github(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            url = f"https://api.github.com/search/issues?q={enc}+state:closed&per_page=5"
            data = self._http_get(url, json_mode=True)
            for it in data.get('items', [])[:5]:
                results.append({
                    'source': 'GitHub',
                    'title': it.get('title', ''),
                    'link': it.get('html_url', ''),
                    'solution': (it.get('body') or '')[:1500],
                })
        except Exception:
            pass
        return results

    def _search_duckduckgo(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://html.duckduckgo.com/html/?q={enc}")
            for link, title in re.findall(
                r'<a[^>]*href="([^"]*)"[^>]*class="result__a"[^>]*>(.*?)</a>',
                html
            )[:5]:
                results.append({
                    'source': 'DuckDuckGo',
                    'title': self._clean_html(title),
                    'link': link,
                    'solution': '',
                })
        except Exception:
            pass
        return results

    def _search_google(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://www.google.com/search?q={enc}&num=5&hl=en")
            for m in re.finditer(r'href="/url\?q=([^&"]+)[^"]*"[^>]*>(.*?)</a>', html):
                u = urllib.parse.unquote(m.group(1))
                t = self._clean_html(m.group(2))
                if t and 'google.' not in u and u.startswith('http'):
                    results.append({'source': 'Google', 'title': t[:200],
                                    'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_bing(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://www.bing.com/search?q={enc}&count=10")
            for m in re.finditer(r'<h2><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', html):
                u, t = m.group(1), self._clean_html(m.group(2))
                if u.startswith('http') and t:
                    results.append({'source': 'Bing', 'title': t[:200],
                                    'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_reddit(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            url = f"https://www.reddit.com/search.json?q={enc}&limit=5&sort=relevance"
            data = self._http_get(url, json_mode=True)
            for c in data.get('data', {}).get('children', [])[:5]:
                p = c.get('data', {})
                results.append({
                    'source': 'Reddit',
                    'title': p.get('title', ''),
                    'link': 'https://reddit.com' + p.get('permalink', ''),
                    'score': p.get('score', 0),
                    'solution': (p.get('selftext') or '')[:1000],
                })
        except Exception:
            pass
        return results

    def _search_arch_wiki(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            url = (f"https://wiki.archlinux.org/api.php?action=query"
                   f"&list=search&srsearch={enc}&format=json&srlimit=5")
            data = self._http_get(url, json_mode=True)
            for it in data.get('query', {}).get('search', [])[:5]:
                t = it.get('title', '')
                results.append({
                    'source': 'Arch Wiki',
                    'title': t,
                    'link': f"https://wiki.archlinux.org/index.php/{urllib.parse.quote(t)}",
                    'solution': self._clean_html(it.get('snippet', '')),
                })
        except Exception:
            pass
        return results

    def _search_searx(self, query: str) -> List[Dict]:
        results = []
        instances = [
            'https://searx.be',
            'https://search.bus-hit.me',
            'https://searx.tiekoetter.com',
            'https://baresearch.org',
        ]
        enc = urllib.parse.quote(query)
        for inst in instances:
            try:
                data = self._http_get(f"{inst}/search?q={enc}&format=json",
                                      timeout=6, json_mode=True)
                for it in data.get('results', [])[:5]:
                    results.append({
                        'source': 'Searx',
                        'title': it.get('title', ''),
                        'link': it.get('url', ''),
                        'solution': (it.get('content') or '')[:500],
                    })
                if results:
                    break
            except Exception:
                continue
        return results

    def _search_yandex(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://yandex.com/search/?text={enc}")
            for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', html):
                u, t = m.group(1), self._clean_html(m.group(2))
                if 'yandex' not in u and t and len(t) > 8:
                    results.append({'source': 'Yandex', 'title': t[:200],
                                    'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_brave(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://search.brave.com/search?q={enc}")
            for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', html):
                u, t = m.group(1), self._clean_html(m.group(2))
                if 'brave.com' not in u and t and len(t) > 5:
                    results.append({'source': 'Brave', 'title': t[:200],
                                    'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_mojeek(self, query: str) -> List[Dict]:
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://www.mojeek.com/search?q={enc}")
            for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', html):
                u, t = m.group(1), self._clean_html(m.group(2))
                if 'mojeek' not in u and t and len(t) > 5:
                    results.append({'source': 'Mojeek', 'title': t[:200],
                                    'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_marginalia(self, query: str) -> List[Dict]:
        """Deep / indie web search (tidak diindeks Google)."""
        results = []
        try:
            enc = urllib.parse.quote(query)
            html = self._http_get(f"https://search.marginalia.nu/search?query={enc}")
            for m in re.finditer(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', html):
                u, t = m.group(1), self._clean_html(m.group(2))
                if 'marginalia' not in u and len(t) > 5:
                    results.append({'source': 'Marginalia',
                                    'title': t[:200], 'link': u, 'solution': ''})
                    if len(results) >= 5:
                        break
        except Exception:
            pass
        return results

    def _search_linux_forums(self, query: str) -> List[Dict]:
        """Deprecated — alias ke Ask Ubuntu."""
        return self._search_stackexchange(query, 'askubuntu')

    # ===============================================================
    # COMMAND EXTRACTION
    # ===============================================================
    def extract_commands(self, solutions: List[Dict]) -> List[str]:
        commands: List[str] = []
        pats = [
            r'```(?:bash|sh|shell)?\s*\n?([^\n`]+)',
            r'`([^`\n]+)`',
            r'(?:^|\n)\s*(?:sudo\s+)?(systemctl|apt|apt-get|yum|dnf|pacman|'
            r'zypper|snap|pip|pip3|journalctl|service|update-rc\.d|dpkg|'
            r'rpm|ip|ifconfig|netstat|ss|route|mount|umount|chmod|chown|'
            r'echo|sysctl|modprobe|rmmod|insmod|kill|pkill|killall|'
            r'nmcli|ufw|iptables|nft|docker|podman|kubectl|swapoff|swapon|'
            r'free|df|du|find|sed|awk|grep|tr|tee)\s+[^\n;]+',
        ]
        for sol in solutions:
            text = (sol.get('title', '') + '\n' + sol.get('solution', ''))
            for p in pats:
                for m in re.findall(p, text, re.IGNORECASE | re.MULTILINE):
                    c = m[0] if isinstance(m, tuple) else m
                    c = c.strip().rstrip('.;,')
                    if 4 < len(c) < 220 and any(k in c for k in (
                        'systemctl', 'apt', 'journalctl', 'service', 'echo',
                        'ip ', 'ifconfig', 'modprobe', 'sysctl', 'ufw', 'iptables',
                        'kill', 'pkill', 'df ', 'du ', 'free ')):
                        commands.append(c)
        seen, uniq = set(), []
        for c in commands:
            if c not in seen:
                seen.add(c)
                uniq.append(c)
        return uniq[:20]

    # ===============================================================
    # IMPROVISE + EXECUTE
    # ===============================================================
    def improvise_fix(self, error_id: str, error_message: str,
                      error_context: Dict = None) -> List[str]:
        fixes: List[str] = []

        # Strategy 1: learning DB (dengan guard dict/str)
        if error_id in self.successful_fixes:
            learned = self.successful_fixes[error_id]
            if learned:
                for item in learned[-5:]:
                    if isinstance(item, dict):
                        cmd = item.get('command', '')
                    elif isinstance(item, str):
                        cmd = item
                    else:
                        cmd = ''
                    if cmd:
                        fixes.append(cmd)
                print(f"{colors.DIM}   📚 {len(learned)} learned solutions{colors.NC}")

        # Strategy 2: pattern DB
        for pattern_id, pattern in self.error_patterns.items():
            for p in pattern.get('patterns', []):
                if re.search(p, error_message, re.IGNORECASE):
                    known = pattern.get('known_fixes', [])
                    fixes.extend(known)
                    print(f"{colors.DIM}   📋 {len(known)} pattern solutions{colors.NC}")
                    break

        # Strategy 3: internet search
        search_terms = []
        for pattern_id, pattern in self.error_patterns.items():
            for p in pattern.get('patterns', []):
                if re.search(p, error_message, re.IGNORECASE):
                    search_terms.extend(pattern.get('search_terms', []))
                    break
        if not search_terms:
            words = re.findall(r'[A-Za-z_]+', error_message)[:5]
            search_terms.append(' '.join(words) + ' linux fix')
            search_terms.append(error_id + ' error fix')

        for term in search_terms[:3]:
            print(f"{colors.DIM}   🌐 Searching: {term[:40]}...{colors.NC}")
            solutions = self.search_internet(term)
            if solutions:
                cmd_fixes = self.extract_commands(solutions)
                if cmd_fixes:
                    fixes.extend(cmd_fixes)
                    break

        # Strategy 4: generic fallback
        if not fixes:
            fixes.extend([
                'systemctl daemon-reload',
                'systemctl reset-failed',
                'journalctl -p err -b --no-pager | tail -50',
                'systemctl list-units --failed',
            ])
            print(f"{colors.DIM}   🔧 generic fallback{colors.NC}")

        # Dedup + guard
        seen, uniq = set(), []
        for fix in fixes:
            if isinstance(fix, dict):
                fix = fix.get('command', '')
            if isinstance(fix, str) and fix and fix not in seen and len(fix) > 3:
                seen.add(fix)
                uniq.append(fix)
        return uniq[:15]

    def try_fix(self, command: str, context: Dict = None) -> Dict:
        result = {'command': command[:120], 'success': False, 'output': '', 'error': ''}
        try:
            print(f"{colors.WHITE}  🔧 Trying: {command[:70]}...{colors.NC}")
            proc = subprocess.run(command, shell=True, capture_output=True,
                                  text=True, timeout=30)
            result['output'] = (proc.stdout or '')[:300]
            result['error'] = (proc.stderr or '')[:300]
            result['success'] = proc.returncode == 0
            if result['success']:
                print(f"{colors.GREEN}    ✅ Success{colors.NC}")
                if context:
                    self._record_success(context.get('error_id', 'unknown'), command)
            else:
                print(f"{colors.RED}    ❌ Failed (code {proc.returncode}){colors.NC}")
                if context:
                    self._record_failure(context.get('error_id', 'unknown'), command)
        except subprocess.TimeoutExpired:
            result['error'] = 'Timeout after 30s'
            print(f"{colors.RED}    ❌ Timeout{colors.NC}")
        except Exception as e:
            result['error'] = str(e)
            print(f"{colors.RED}    ❌ Error: {str(e)[:50]}{colors.NC}")
        return result

    def _record_success(self, error_id: str, command: str):
        self.successful_fixes[error_id].append({
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.successful_fixes[error_id]) > 20:
            self.successful_fixes[error_id] = self.successful_fixes[error_id][-20:]
        self.ai_solutions_count += 1
        self._save_learning_db()

    def _record_failure(self, error_id: str, command: str):
        self.failed_attempts[error_id].append({
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.failed_attempts[error_id]) > 20:
            self.failed_attempts[error_id] = self.failed_attempts[error_id][-20:]
        self._save_learning_db()

    def smart_fix(self, error: Dict, progress_callback=None) -> Dict:
        error_id = error.get('error_id', 'UNKNOWN')
        error_message = error.get('message', '')
        if progress_callback:
            progress_callback('ai', f"🧠 AI analyzing: {error_id}")

        print(f"\n{colors.PURPLE}🧠 AI Improvising: {error_id}{colors.NC}")
        print(f"{colors.DIM}   Message: {error_message[:80]}{colors.NC}")

        fixes = self.improvise_fix(error_id, error_message, error)
        if not fixes:
            return {'error_id': error_id, 'success': False,
                    'message': 'No solution found',
                    'attempted_commands': [], 'successful_commands': []}

        print(f"{colors.YELLOW}📋 Testing {len(fixes)} solutions{colors.NC}")
        attempted, successful = [], []
        for i, fix_cmd in enumerate(fixes[:15], 1):
            if progress_callback:
                progress_callback('detail', f"[{i}/{min(len(fixes), 15)}] {fix_cmd[:50]}...")
            result = self.try_fix(fix_cmd, {'error_id': error_id})
            attempted.append(fix_cmd)
            if result['success']:
                successful.append(fix_cmd)
                if progress_callback:
                    progress_callback('success', f"✅ {fix_cmd[:50]}...")
                if len(successful) >= 2:
                    break
            else:
                if progress_callback:
                    progress_callback('error', f"❌ {fix_cmd[:50]}...")

        return {
            'error_id': error_id,
            'success': len(successful) > 0,
            'message': f"Found {len(successful)} working solutions",
            'attempted_commands': attempted[:10],
            'successful_commands': successful[:5]
        }

    def get_error_summary(self, errors: List[Dict]) -> Dict:
        systemd_count = 0
        other_count = 0
        unique_errors = set()
        for error in errors:
            err_id = error.get('error_id', 'UNKNOWN')
            unique_errors.add(err_id)
            if 'SYSTEMD' in err_id or 'systemd' in error.get('message', '').lower():
                systemd_count += 1
            else:
                other_count += 1
        return {
            'systemd_count': systemd_count,
            'other_count': other_count,
            'unique_count': len(unique_errors),
            'ai_solutions': self.ai_solutions_count
        }

#===============================================================================
# PROGRESS TRACKER
#===============================================================================
class ProgressTracker:
    def __init__(self):
        self.threads = {}
        self.lock = threading.Lock()

    def create(self, thread_id: str, total: int) -> Dict:
        with self.lock:
            self.threads[thread_id] = {
                'id': thread_id, 'total': total, 'current': 0, 'percent': 0,
                'status': 'running', 'current_fix': 'Initializing AI...',
                'details': [], 'start_time': datetime.now().isoformat()
            }
            return self.threads[thread_id]

    def update(self, thread_id, current, current_fix=None, detail=None, detail_type='info'):
        with self.lock:
            if thread_id not in self.threads:
                return
            t = self.threads[thread_id]
            t['current'] = current
            t['percent'] = int((current / t['total']) * 100) if t['total'] > 0 else 0
            if current_fix:
                t['current_fix'] = current_fix
            if detail:
                t['details'].append({
                    'timestamp': datetime.now().isoformat(),
                    'message': detail, 'type': detail_type
                })

    def complete(self, thread_id: str, results: Dict):
        with self.lock:
            if thread_id in self.threads:
                self.threads[thread_id]['status'] = 'complete'
                self.threads[thread_id]['results'] = results

    def get(self, thread_id: str) -> Optional[Dict]:
        with self.lock:
            return self.threads.get(thread_id)

    def stop(self, thread_id: str):
        with self.lock:
            if thread_id in self.threads:
                self.threads[thread_id]['status'] = 'stopped'

#===============================================================================
# HTTP SERVER WITH SSE
#===============================================================================
class HTTPServer:
    def __init__(self, port=8080):
        self.port = port
        self.server = None
        self.engine = None
        self.progress = ProgressTracker()
        self.fix_threads = {}

    def set_engine(self, engine):
        self.engine = engine

    def start(self):
        try:
            import http.server
            import socketserver

            class Handler(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    if self.path == '/':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html; charset=utf-8')
                        self.end_headers()
                        self.wfile.write(WEB_UI_HTML.encode('utf-8'))

                    elif self.path.startswith('/fix/progress'):
                        self.send_response(200)
                        self.send_header('Content-Type', 'text/event-stream')
                        self.send_header('Cache-Control', 'no-cache')
                        self.send_header('Connection', 'keep-alive')
                        self.end_headers()

                        thread_id = None
                        if '?' in self.path:
                            for p in self.path.split('?')[1].split('&'):
                                if p.startswith('thread_id='):
                                    thread_id = p.split('=')[1]
                        if not thread_id:
                            return

                        last_pct = -1
                        sent_details = 0
                        try:
                            while True:
                                prog = self.server.progress.get(thread_id)
                                if not prog:
                                    break
                                if prog['percent'] != last_pct:
                                    last_pct = prog['percent']
                                    data = {
                                        'type': 'progress',
                                        'percent': prog['percent'],
                                        'current': prog['current'],
                                        'total': prog['total'],
                                        'status': prog['status'],
                                        'current_fix': prog.get('current_fix', '')
                                    }
                                    self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                    self.wfile.flush()

                                details = prog.get('details', [])
                                if details:
                                    for detail in details[sent_details:]:
                                        dt = detail.get('type', 'info')
                                        data = {
                                            'type': 'detail' if dt != 'ai' else 'ai',
                                            'message': detail.get('message', ''),
                                            'success': dt == 'success'
                                        }
                                        self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                        self.wfile.flush()
                                        sent_details += 1
                                    prog['details'] = []

                                if prog['status'] == 'complete':
                                    results = prog.get('results', {})
                                    data = {
                                        'type': 'complete',
                                        'fixes_applied': results.get('fixes_applied', 0),
                                        'unresolved': results.get('unresolved', 0),
                                        'health_score': results.get('health_score', 100)
                                    }
                                    self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                    self.wfile.flush()
                                    break
                                if prog['status'] == 'stopped':
                                    self.wfile.write(b"data: " + json.dumps({'type': 'stopped'}).encode() + b"\n\n")
                                    self.wfile.flush()
                                    break
                                time.sleep(0.5)
                        except (BrokenPipeError, ConnectionResetError):
                            pass

                    else:
                        self.send_response(404)
                        self.end_headers()

                def do_POST(self):
                    if self.path == '/diagnostic':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        if self.server.engine:
                            results = self.server.engine.run_diagnostic()
                            self.wfile.write(json.dumps(results).encode())
                        else:
                            self.wfile.write(json.dumps({'error': 'no engine'}).encode())

                    elif self.path == '/fix/start':
                        # WAJIB baca body walau hanya mode
                        cl = int(self.headers.get('Content-Length', 0) or 0)
                        body_raw = self.rfile.read(cl).decode() if cl > 0 else '{}'
                        try:
                            mode = json.loads(body_raw).get('mode', 'full')
                        except Exception:
                            mode = 'full'

                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()

                        thread_id = str(uuid.uuid4())[:8]
                        errors = self.server.engine.errors if self.server.engine else []
                        total = len(errors)
                        if total == 0:
                            self.wfile.write(json.dumps(
                                {'thread_id': thread_id, 'status': 'no_errors'}).encode())
                            return
                        self.server.progress.create(thread_id, total)

                        def run_ai_fixes():
                            try:
                                progress = self.server.progress
                                improvisor = self.server.engine.improvisor if self.server.engine else None
                                applied, unresolved = 0, 0
                                errs = self.server.engine.errors
                                error_summary = improvisor.get_error_summary(errs) if improvisor else {}
                                progress.update(thread_id, 0, "🧠 AI Engine Starting",
                                                "🧠 AI Improvisation Engine active", 'ai')
                                for i, error in enumerate(errs):
                                    td = progress.get(thread_id)
                                    if td and td['status'] == 'stopped':
                                        break
                                    error_id = error.get('error_id', 'UNKNOWN')
                                    progress.update(thread_id, i, f"🧠 AI: {error_id}")
                                    if improvisor:
                                        result = improvisor.smart_fix(
                                            error,
                                            lambda t, m, i=i, eid=error_id:
                                                progress.update(thread_id, i, f"🧠 {eid}",
                                                                m, 'ai' if t == 'ai' else 'info')
                                        )
                                        if result.get('success'):
                                            applied += 1
                                            progress.update(thread_id, i, f"✅ {error_id} fixed",
                                                            f"✅ AI fixed {error_id}", 'success')
                                        else:
                                            unresolved += 1
                                            progress.update(thread_id, i, f"❌ {error_id}",
                                                            f"❌ Could not fix {error_id}", 'error')
                                    else:
                                        unresolved += 1
                                health_score = max(0, 100 - unresolved * 10)
                                results = {
                                    'fixes_applied': applied,
                                    'unresolved': unresolved,
                                    'health_score': health_score,
                                    'error_summary': error_summary
                                }
                                progress.complete(thread_id, results)
                            except Exception as e:
                                progress.update(thread_id, 0, f"Error: {str(e)}",
                                                f"❌ AI Error: {str(e)}", 'error')
                                progress.complete(thread_id, {'error': str(e)})

                        th = threading.Thread(target=run_ai_fixes, daemon=True)
                        th.start()
                        self.server.fix_threads[thread_id] = th
                        self.wfile.write(json.dumps(
                            {'thread_id': thread_id, 'status': 'started'}).encode())

                    elif self.path == '/fix/stop':
                        cl = int(self.headers.get('Content-Length', 0) or 0)
                        body = self.rfile.read(cl).decode() if cl > 0 else '{}'
                        try:
                            data = json.loads(body)
                        except Exception:
                            data = {}
                        thread_id = data.get('thread_id')

                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        if thread_id:
                            self.server.progress.stop(thread_id)
                            self.wfile.write(json.dumps({'message': 'Stopped by user'}).encode())
                        else:
                            self.wfile.write(json.dumps({'error': 'No thread_id'}).encode())

                    else:
                        self.send_response(404)
                        self.end_headers()

                def log_message(self, fmt, *args):
                    pass

            class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
                allow_reuse_address = True
                daemon_threads = True

            self.server = ThreadingTCPServer(("0.0.0.0", self.port), Handler)
            self.server.progress = self.progress
            self.server.engine = self.engine
            self.server.fix_threads = self.fix_threads

            t = threading.Thread(target=self.server.serve_forever, daemon=True)
            t.start()
            return True
        except Exception as e:
            print(f"{colors.RED}Failed to start web server: {e}{colors.NC}")
            return False

    def stop(self):
        if self.server:
            self.server.shutdown()

#===============================================================================
# SYSTEM INFO
#===============================================================================
class SystemInfo:
    @staticmethod
    def get_cpu_count() -> int:
        try:
            return os.cpu_count() or 1
        except Exception:
            return 1

    @staticmethod
    def get_memory_info() -> Dict:
        try:
            with open('/proc/meminfo', 'r') as f:
                mem = {}
                for line in f:
                    parts = line.split(':')
                    if len(parts) == 2:
                        mem[parts[0].strip()] = int(parts[1].strip().split()[0])
                total = mem.get('MemTotal', 0)
                avail = mem.get('MemAvailable', 0)
                used = total - avail
                pct = (used / total * 100) if total > 0 else 0
                return {'total': total * 1024, 'used': used * 1024, 'percent': round(pct, 2)}
        except Exception:
            return {'total': 0, 'used': 0, 'percent': 0}

    @staticmethod
    def get_disk_usage(path: str = '/') -> Dict:
        try:
            st = os.statvfs(path)
            total = st.f_blocks * st.f_frsize
            free = st.f_bfree * st.f_frsize
            used = total - free
            pct = (used / total * 100) if total > 0 else 0
            return {'total': total, 'used': used, 'percent': round(pct, 2)}
        except Exception:
            return {'total': 0, 'used': 0, 'percent': 0}

    @staticmethod
    def get_uptime() -> str:
        try:
            with open('/proc/uptime', 'r') as f:
                sec = float(f.readline().split()[0])
                d = int(sec // 86400)
                h = int((sec % 86400) // 3600)
                m = int((sec % 3600) // 60)
                if d > 0: return f"{d}d {h}h {m}m"
                if h > 0: return f"{h}h {m}m"
                return f"{m}m"
        except Exception:
            return "Unknown"

#===============================================================================
# ERROR DETECTOR
#===============================================================================
class ErrorDetector:
    def __init__(self):
        self.patterns = {
            'SYSTEMD_FAILURE': {
                'patterns': [r'Failed to query local AF_VSOCK CID',
                             r'systemd-ssh-generator.*failed',
                             r'sd-exec.*failed', r'vsock.*error'],
                'severity': 'critical'
            },
            'SERVICE_CRASHED': {
                'patterns': [r'service.*failed', r'process.*crashed',
                             r'segfault', r'core dumped'],
                'severity': 'critical'
            },
            'SERVICE_TIMEOUT': {
                'patterns': [r'Watchdog timeout', r'Timed out', r'service.*timeout'],
                'severity': 'warning'
            },
            'MEMORY_HIGH': {
                'patterns': [r'Out of memory', r'oom-killer', r'memory.*high'],
                'severity': 'warning'
            },
            'DISK_FULL': {
                'patterns': [r'No space left', r'disk full', r'ENOSPC'],
                'severity': 'critical'
            },
            'NETWORK_ERROR': {
                'patterns': [r'connection timed out', r'network.*failed',
                             r'Cannot connect'],
                'severity': 'warning'
            },
            'PACKAGE_ERROR': {
                'patterns': [r'broken package', r'unmet dependencies', r'dpkg.*error'],
                'severity': 'critical'
            }
        }

    def detect(self, line: str) -> Optional[Dict]:
        for err_id, info in self.patterns.items():
            for pattern in info['patterns']:
                if re.search(pattern, line, re.IGNORECASE):
                    return {'error_id': err_id, 'severity': info['severity'],
                            'message': line.strip()}
        return None

#===============================================================================
# DIAGNOSTIC ENGINE
#===============================================================================
class DiagnosticEngine:
    def __init__(self):
        self.errors = []
        self.fixes_applied = 0
        self.health_score = 100
        self.detector = ErrorDetector()
        self.improvisor = ImprovisationEngine()

    def run_diagnostic(self) -> Dict:
        self.errors = []
        self.health_score = 100
        print(f"{colors.YELLOW}🔍 Running diagnostic scan...{colors.NC}")
        self._check_logs()
        self._check_services()
        self._check_resources()

        critical = len([e for e in self.errors if e.get('severity') == 'critical'])
        warnings = len([e for e in self.errors if e.get('severity') == 'warning'])
        self.health_score = max(0, 100 - critical * 10 - warnings * 3)
        error_summary = self.improvisor.get_error_summary(self.errors)

        print(f"{colors.GREEN}✅ Scan complete: {len(self.errors)} errors{colors.NC}")
        print(f"{colors.DIM}   Critical: {critical}, Warnings: {warnings}{colors.NC}")
        print(f"{colors.DIM}   SYSTEMD errors: {error_summary['systemd_count']}{colors.NC}")
        print(f"{colors.PURPLE}🧠 AI has {error_summary['ai_solutions']} learned solutions{colors.NC}")

        return {
            'errors': self.errors,
            'summary': {
                'total_errors': len(self.errors),
                'critical_errors': critical,
                'warnings': warnings,
                'health_score': self.health_score
            },
            'error_summary': error_summary,
            'fixes_applied': self.fixes_applied
        }

    def _check_logs(self):
        log_files = ['/var/log/syslog', '/var/log/messages', '/var/log/kern.log']
        for log_file in log_files:
            if os.path.exists(log_file):
                try:
                    with open(log_file, 'r', errors='ignore') as f:
                        for line in f.readlines()[-500:]:
                            err = self.detector.detect(line)
                            if err:
                                self.errors.append(err)
                except Exception:
                    pass

        if shutil.which('journalctl'):
            try:
                result = subprocess.run(
                    ['journalctl', '-p', 'err', '-b', '--no-pager', '-n', '300'],
                    capture_output=True, text=True, timeout=10, check=False
                )
                for line in result.stdout.split('\n'):
                    err = self.detector.detect(line)
                    if err:
                        self.errors.append(err)
            except Exception:
                pass

    def _check_services(self):
        if shutil.which('systemctl'):
            try:
                result = subprocess.run(
                    ['systemctl', '--failed', '--no-pager'],
                    capture_output=True, text=True, timeout=5, check=False
                )
                for line in result.stdout.split('\n'):
                    if '.service' in line and '●' not in line and line.strip():
                        parts = line.split()
                        if parts:
                            self.errors.append({
                                'error_id': 'SERVICE_CRASHED',
                                'severity': 'critical',
                                'message': f'Service {parts[0]} failed',
                                'service': parts[0]
                            })
            except Exception:
                pass

    def _check_resources(self):
        mem = SystemInfo.get_memory_info()
        if mem.get('percent', 0) > 90:
            self.errors.append({
                'error_id': 'MEMORY_HIGH', 'severity': 'warning',
                'message': f'Memory usage: {mem["percent"]}%'
            })
        disk = SystemInfo.get_disk_usage('/')
        if disk.get('percent', 0) > 90:
            self.errors.append({
                'error_id': 'DISK_FULL', 'severity': 'critical',
                'message': f'Disk usage: {disk["percent"]}%'
            })

#===============================================================================
# MAIN APPLICATION
#===============================================================================
class AutoFixDetectAI:
    def __init__(self):
        self.colors = colors
        self.engine = DiagnosticEngine()
        self.web_server = None
        self.start_time = datetime.now()

    def print_banner(self):
        print(f"""
{self.colors.CYAN}{self.colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           AUTOFIXDETECT AI v{VERSION} - {VERSION_NAME}              ║
║                                                                            ║
║   ⚡ AI-Powered System Diagnostic & Auto-Fix Tool                          ║
║   🧠 Self-Learning with 16-Source Search & Improvisation                  ║
║   🌐 Full Web Interface with Real-Time Progress                           ║
║   📚 No External Dependencies - Fully Self-Contained                      ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
{self.colors.NC}
{self.colors.WHITE}📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{self.colors.NC}
{self.colors.DIM}🖥️  {socket.gethostname()} | {SystemInfo.get_cpu_count()} cores | {SystemInfo.get_uptime()} uptime{self.colors.NC}
{self.colors.DIM}🐍 Python {sys.version.split()[0]} | {platform.platform()}{self.colors.NC}
{self.colors.PURPLE}🧠 AI Engine: Active | 16-Source Search: Enabled{self.colors.NC}
""")

    def start_web(self):
        self.web_server = HTTPServer(8080)
        self.web_server.set_engine(self.engine)
        if self.web_server.start():
            print(f"{self.colors.GREEN}🌐 Web interface: http://localhost:8080{colors.NC}")
            print(f"{self.colors.PURPLE}🧠 AI Improvisation Engine active (16 sources){colors.NC}")
            print(f"{self.colors.GREEN}   Press Ctrl+C to stop{colors.NC}")
            return True
        return False

    def run_cli(self):
        self.print_banner()
        print(f"{self.colors.YELLOW}🔍 Running AI-powered diagnostic...{self.colors.NC}")
        results = self.engine.run_diagnostic()
        summary = results['summary']
        error_summary = results.get('error_summary', {})

        print(f"\n{self.colors.WHITE}{self.colors.BOLD}📊 Results:{self.colors.NC}")
        print(f"  ❤️  Health: {summary['health_score']}/100")
        print(f"  📌 Total Errors: {summary['total_errors']}")
        print(f"  🔴 Critical: {summary['critical_errors']}")
        print(f"  🟡 Warnings: {summary['warnings']}")
        print(f"  📚 SYSTEMD Errors: {error_summary.get('systemd_count', 0)}")
        print(f"  🧠 AI Solutions: {error_summary.get('ai_solutions', 0)}")

        if results['errors']:
            print(f"\n{self.colors.RED}📋 Error Details:{self.colors.NC}")
            for i, e in enumerate(results['errors'][:10], 1):
                sev = e.get('severity', 'unknown')
                color = self.colors.RED if sev == 'critical' else self.colors.YELLOW
                print(f"  {i}. {color}[{sev.upper()}]{self.colors.NC} {e.get('error_id', 'UNKNOWN')}")
                print(f"     {self.colors.DIM}{e.get('message', '')[:80]}{self.colors.NC}")
            if len(results['errors']) > 10:
                print(f"  {self.colors.DIM}... and {len(results['errors']) - 10} more{self.colors.NC}")

            print(f"\n{self.colors.PURPLE}🧠 AI Engine ready to improvise solutions...{self.colors.NC}")
            try:
                resp = input(f"\n{self.colors.WHITE}Run AI fixes? (y/n): {self.colors.NC}")
            except (EOFError, KeyboardInterrupt):
                resp = 'n'

            if resp.lower() in ['y', 'yes']:
                print(f"\n{self.colors.YELLOW}🧠 AI Improvising...{self.colors.NC}")
                fixed = 0
                for error in results['errors']:
                    result = self.engine.improvisor.smart_fix(error)
                    if result['success']:
                        fixed += 1
                        print(f"{self.colors.GREEN}✅ {result['error_id']} fixed{self.colors.NC}")
                    else:
                        print(f"{self.colors.RED}❌ {result['error_id']} unresolved{self.colors.NC}")
                print(f"\n{self.colors.GREEN}✅ AI fixed {fixed}/{len(results['errors'])} errors{self.colors.NC}")
                if fixed < len(results['errors']):
                    print(f"{self.colors.YELLOW}⚠ {len(results['errors']) - fixed} errors need manual intervention{self.colors.NC}")
        else:
            print(f"\n{self.colors.GREEN}🎉 No errors detected! System is healthy.{self.colors.NC}")

    def run(self):
        if '--web' in sys.argv or '-w' in sys.argv:
            self.print_banner()
            if self.start_web():
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print(f"\n{self.colors.YELLOW}⏹ Shutting down web interface...{self.colors.NC}")
                    if self.web_server:
                        self.web_server.stop()
                    print(f"{self.colors.GREEN}✅ Done.{self.colors.NC}")
            else:
                print(f"{self.colors.RED}Failed to start web interface.{self.colors.NC}")
                self.run_cli()
        else:
            self.run_cli()

#===============================================================================
# ENTRY POINT
#===============================================================================
if __name__ == "__main__":
    if sys.version_info < (3, 6):
        print("Python 3.6+ required.")
        sys.exit(1)

    def signal_handler(sig, frame):
        print(f"\n{colors.YELLOW}⏹ Interrupted by user.{colors.NC}")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    app = AutoFixDetectAI()
    app.run()
