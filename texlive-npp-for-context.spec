Name:		texlive-npp-for-context
Version:	51389
Release:	2
Summary:	ConTeXt plugin for Notepad++
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/npp-for-context
License:	noinfo
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/npp-for-context.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/npp-for-context.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides A plugin for Notepad++ that implements,
for the ConTeXt document processing system, a language lexer
for semantic highlighting of TeX, LuaTeX, and ConTeXt commands;
autocompletion of commands with full support for calltips (set
in columns); tagging and insertion of markup and templates,
with support for mnemonic keys. A color scheme and two
complementary Notepad++ themes: "Silver Twilight Hi" and
"Silver Twilight Lo".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/context/third/npp-for-context

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
