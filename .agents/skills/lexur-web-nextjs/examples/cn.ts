// src/lib/cn.ts
// tailwind-merge (v3, Tailwind v4) debe conocer la escala LEXUR; si no, trata `text-h1` (tamano)
// y `text-fg` (color) como la misma utilidad y elimina una de ellas.
import { clsx, type ClassValue } from 'clsx';
import { extendTailwindMerge } from 'tailwind-merge';

const twMerge = extendTailwindMerge({
  extend: {
    theme: {
      text: [
        'display-xl', 'display', 'h1', 'h2', 'h3', 'h4', 'body-lg', 'body', 'body-sm',
        'label', 'caption', 'overline', 'metric',
      ],
      color: [
        'canvas', 'surface-1', 'surface-2', 'surface-3', 'inverse',
        'line-subtle', 'line', 'line-strong', 'line-control',
        'fg', 'fg-muted', 'fg-subtle', 'fg-disabled', 'fg-inverse', 'on-accent',
        'accent', 'accent-hover', 'accent-pressed', 'accent-subtle', 'accent-fg',
        'success', 'success-subtle', 'warning', 'warning-subtle', 'danger', 'danger-subtle',
        'focus', 'scrim',
      ],
      radius: ['none', 'xs', 'sm', 'md', 'lg', 'xl', 'full'],
      ease: ['standard', 'enter', 'exit'],
    },
  },
});

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
