import type { Metadata } from 'next';
import { Plus_Jakarta_Sans, Outfit, JetBrains_Mono } from 'next/font/google';
import './globals.css';
import { ThemeProvider } from '@/context/ThemeContext';
import { ModalProvider } from '@/context/ModalContext';
import { Navbar } from '@/components/common/Navbar/Navbar';
import { Footer } from '@/components/common/Footer/Footer';
import { CaseStudyModal } from '@/components/common/Modal/CaseStudyModal';
import { siteConfig } from '@/data/siteConfig';

const jakarta = Plus_Jakarta_Sans({
  subsets: ['latin'],
  weight: ['300', '400', '500', '600', '700', '800'],
  variable: '--font-jakarta',
  display: 'swap',
});

const outfit = Outfit({
  subsets: ['latin'],
  weight: ['400', '600', '700', '800'],
  variable: '--font-outfit',
  display: 'swap',
});

const jetbrains = JetBrains_Mono({
  subsets: ['latin'],
  weight: ['400', '600', '700'],
  variable: '--font-jetbrains',
  display: 'swap',
});

export const metadata: Metadata = {
  title: `${siteConfig.name} | Data Analyst & Business Intelligence Specialist`,
  description:
    'Portfolio of Sanjeet Kumar - Data Analyst specializing in Python, Machine Learning, Banking Credit Risk Analytics, and Adidas Sales Business Intelligence.',
  keywords: [
    'Data Analyst',
    'Sanjeet Kumar',
    'Business Intelligence',
    'Python',
    'Pandas',
    'Credit Risk Analytics',
    'Adidas Sales Analysis',
    'Tableau',
    'MySQL',
  ],
  authors: [{ name: siteConfig.name }],
  openGraph: {
    title: `${siteConfig.name} | Data Analyst Portfolio`,
    description:
      'Explore end-to-end data analytics projects including Banking Credit Risk Modeling and Adidas US Sales Analytics.',
    type: 'website',
    url: siteConfig.socialLinks.linkedin,
    siteName: siteConfig.brandName,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="dark" className={`${jakarta.variable} ${outfit.variable} ${jetbrains.variable}`}>
      <head>
        {/* Anti-FOUC theme detection script */}
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var theme = localStorage.getItem('sanjeet_portfolio_theme') || 'dark';
                  document.documentElement.setAttribute('data-theme', theme);
                } catch(e) {}
              })();
            `,
          }}
        />
      </head>
      <body>
        <ThemeProvider>
          <ModalProvider>
            <Navbar />
            <main>{children}</main>
            <Footer />
            <CaseStudyModal />
          </ModalProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
