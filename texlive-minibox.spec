Name:		texlive-minibox
Version:	30914
Release:	2
Summary:	A simple type of box for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minibox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minibox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package provides a convenient input syntax for boxes
that don't break their text over lines automatically, but do
allow manual line breaks. The boxes shrink to the natural width
of the longest line they contain.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minibox/minibox.sty
%doc %{_texmfdistdir}/doc/latex/minibox/README
%doc %{_texmfdistdir}/doc/latex/minibox/minibox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/minibox/minibox.ins
%doc %{_texmfdistdir}/source/latex/minibox/minibox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
