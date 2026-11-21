'use client';

import React from 'react';
import { useTheme } from '@/context/ThemeContext';
import { SunIcon, MoonIcon } from '../Icons/Icons';

export function ThemeToggle({ className = '' }: { className?: string }) {
  const { theme, toggleTheme } = useTheme();

  return (
    <button
      onClick={toggleTheme}
      className={`theme-toggle-btn ${className}`}
      aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
      title={`Switch to ${theme === 'dark' ? 'Vibrant Color / Light' : 'Deep Cyber Dark'} Mode`}
      style={{
        width: '42px',
        height: '42px',
        borderRadius: '10px',
        background: 'var(--bg-card)',
        border: '1px solid var(--border-light)',
        color: 'var(--text-primary)',
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        cursor: 'pointer',
        transition: 'all 0.2s ease',
      }}
    >
      {theme === 'dark' ? (
        <SunIcon size={18} style={{ color: '#F59E0B' }} />
      ) : (
        <MoonIcon size={18} style={{ color: '#6366F1' }} />
      )}
    </button>
  );
}
