Name:		texlive-he-she
Version:	41359
Release:	2
Summary:	Alternating pronouns to aid to gender-neutral writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/he-she
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements a version of semi-automatic pronoun
switching for writing gender-neutral (and possibly annoying)
prose. It has upper- and lowercase versions of switching
pronouns for all case forms, plus anaphoric versions that
reflect the current gender choice.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/he-she/he-she.sty
%doc %{_texmfdistdir}/doc/latex/he-she/README
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.pdf
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
