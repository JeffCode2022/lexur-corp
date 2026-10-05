// src/components/ui/lx-button.tsx — patron de referencia para las primitivas LEXUR.
import { forwardRef, type ButtonHTMLAttributes, type ReactNode } from 'react';
import { Loader2 } from 'lucide-react';
import { cn } from '@/lib/cn';

type Variant = 'primary' | 'accent' | 'secondary' | 'ghost' | 'danger';
type Size = 'sm' | 'md' | 'lg';

const base =
  'inline-flex items-center justify-center gap-2 font-medium select-none whitespace-nowrap ' +
  'transition-[background-color,color,transform] duration-[var(--lx-duration-instant)] ease-standard ' +
  'active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus ' +
  'disabled:pointer-events-none disabled:text-fg-disabled aria-disabled:pointer-events-none';

const variants: Record<Variant, string> = {
  primary: 'bg-inverse text-fg-inverse hover:bg-inverse/90 disabled:bg-surface-2',
  accent: 'bg-accent text-on-accent hover:bg-accent-hover active:bg-accent-pressed disabled:bg-surface-2',
  secondary: 'bg-surface-2 text-fg border border-line hover:bg-surface-3',
  ghost: 'bg-transparent text-fg hover:bg-surface-2',
  danger: 'bg-danger text-fg-inverse hover:bg-danger/90 disabled:bg-surface-2',
};

const sizes: Record<Size, string> = {
  sm: 'h-8 px-3 text-body-sm rounded-sm',
  md: 'h-10 px-4 text-label rounded-md',
  lg: 'h-12 px-5 text-body rounded-md',
};

export interface LxButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  size?: Size;
  loading?: boolean;
  icon?: ReactNode;
}

export const LxButton = forwardRef<HTMLButtonElement, LxButtonProps>(function LxButton(
  { variant = 'primary', size = 'md', loading = false, icon, className, children, disabled, type = 'button', ...props },
  ref,
) {
  return (
    <button
      ref={ref}
      type={type}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      className={cn(base, variants[variant], sizes[size], className)}
      {...props}
    >
      {loading ? <Loader2 className="size-4 animate-spin" strokeWidth={1.5} aria-hidden /> : icon}
      {children}
    </button>
  );
});

// Nota: en tema light `danger` usa text-on-accent (blanco). Si el proyecto lo requiere, resolverlo con
// un token dedicado `danger.on` en tokens.json en vez de condicionales por tema en el componente.
