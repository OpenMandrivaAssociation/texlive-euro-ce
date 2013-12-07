# revision 25714
# category Package
# catalog-ctan /fonts/euro-ce
# catalog-date 2012-03-20 10:39:30 +0100
# catalog-license bsd
# catalog-version 3.0b
Name:		texlive-euro-ce
Epoch:		1
Version:	3.0b
Release:	4
Summary:	Euro and CE sign font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/euro-ce
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Metafont source for the symbols in several variants, designed
to fit with Computer Modern-set text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/euro-ce/ceit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cemac.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cerm.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cesl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobf.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobfit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobfsl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euroit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euromac.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euroof.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurorm.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurosl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurosp.mf
%{_texmfdistdir}/fonts/tfm/public/euro-ce/ceit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/cerm.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/cesl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobf.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobfit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobfsl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/euroit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/euroof.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurorm.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurosl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurosp.tfm
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.doc
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.dvi
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:3.0b-1
+ Revision: 787588
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070729-2
+ Revision: 751665
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070729-1
+ Revision: 718388
- texlive-euro-ce
- texlive-euro-ce
- texlive-euro-ce
- texlive-euro-ce

